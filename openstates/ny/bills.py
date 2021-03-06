import re
import datetime

from billy.scrape.bills import BillScraper, Bill

import scrapelib
import lxml.html
import lxml.etree


class NYBillScraper(BillScraper):
    state = 'ny'

    def scrape(self, chamber, session):
        try:
            for index in xrange(1, 1000):
                url = ("http://open.nysenate.gov/legislation/search/"
                       "?search=otype:bill&searchType=&format=xml"
                       "&pageIdx=%d" % index)
                with self.urlopen(url) as page:
                    page = lxml.etree.fromstring(page)

                    for result in page.xpath("//result[@type = 'bill']"):
                        id = result.attrib['id'].split('-')[0]

                        title = result.attrib['title'].strip()
                        if title == '(no title)':
                            continue

                        primary_sponsor = result.attrib['sponsor']

                        if id.startswith('S'):
                            bill_chamber = 'upper'
                        else:
                            bill_chamber = 'lower'

                        if chamber != bill_chamber:
                            continue

                        bill = Bill(session, chamber, id, title)
                        bill.add_source(url)
                        bill.add_sponsor('primary', primary_sponsor)

                        bill_url = ("http://open.nysenate.gov/legislation/"
                                    "bill/%s" % result.attrib['id'])
                        self.scrape_bill(bill, bill_url)
                        bill.add_source(bill_url)

                        self.save_bill(bill)
        except scrapelib.HTTPError as e:
            if e.response.code != 404:
                raise

    def scrape_bill(self, bill, url):
        with self.urlopen(url) as page:
            page = lxml.html.fromstring(page)
            page.make_links_absolute(url)

            actions = []
            for li in page.xpath("//div[@id = 'content']/ul[1]/li"):
                text = li.text.strip()

                match = re.match(r"([A-Z][a-z][a-z]\s+\d{1,2},\s+\d{4,4}):"
                                 r"\s+(.*)$", text)
                date = datetime.datetime.strptime(match.group(1),
                                                  "%b %d, %Y").date()
                action = match.group(2)

                actions.append((date, action))

            first = True
            act_chamber = bill['chamber']
            for date, action in reversed(actions):
                atype = []
                if first:
                    atype.append('bill:introduced')
                    first = False

                if 'REFERRED TO' in action:
                    atype.append('committee:referred')
                elif action == 'ADOPTED':
                    atype.append('bill:passed')
                elif action in ('PASSED SENATE', 'PASSED ASSEMBLY'):
                    atype.append('bill:passed')
                elif action in ('DELIVERED TO SENATE',
                                'DELIVERED TO ASSEMBLY'):
                    first = True
                    act_chamber = {'upper': 'lower',
                                   'lower': 'upper'}[act_chamber]
                elif (action.startswith('AMENDED') or
                      action.startswith('AMEND (T) AND')):
                    atype.append('amendment:passed')
                elif action.startswith('RECOMMIT,'):
                    atype.append('committee:referred')

                if 'RECOMMIT TO' in action:
                    atype.append('committee:referred')

                if not atype:
                    atype = ['other']

                bill.add_action(bill['chamber'], action, date,
                                type=atype)

            text_link = page.xpath("//a[contains(@href, 'lrs-print')]")[0]
            bill.add_version(bill['bill_id'], text_link.attrib['href'])

            subjects = []
            for link in page.xpath("//a[contains(@href, 'lawsection')]"):
                subjects.append(link.text.strip())
            bill['subjects'] = subjects
