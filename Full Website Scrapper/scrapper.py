import os
cls = lambda: os.system('cls')

from requests_html import HTMLSession
import csv

site = 'https://www.ecufiles.com/specifications/'

file = open('ecufiles.csv','w')
csv_writer = csv.writer(file)

header = ['Brand','Series','Generation','Specification',
'Original Power','Original Couple','After Tuning Power',
'After Tuning Couple','Difference Power','Difference Couple']

csv_writer.writerow(header)

total_requests = 0 
total_scrapped_data = 0

def brand_pipeline(link):
    brand_selector_id = 'brand-selector'
    # session = HTMLSession()
    session = AsyncHTMLSession()
    response = session.get(link)
    total_requests = total_requests + 1
    total_scrapped_data = total_scrapped_data + len(response.html.html)
    html = response.html
    # html.render()
    brand_selector = html.find('#{}'.format(brand_selector_id),first=True)
    options_list = brand_selector.find('option')
    toggle = True
    for option in options_list:
        if toggle:
            toggle = False
            continue
        #print('link: {} name: {}'.format(option.attrs['value'],option.text))
        link = option.attrs['value']
        br_name = option.text
        print('Scaning: {}'.format(br_name))        
        series_pipeline(link,br_name)
        # print(link)


def series_pipeline(link,br_name):
    series_selector_id = 'series-selector'
    # session = HTMLSession()
    session = AsyncHTMLSession()
    response = session.get(link)
    total_requests = total_requests + 1
    total_scrapped_data = total_scrapped_data + len(response.html.html)
    html = response.html
    # html.render()
    series_selector = html.find('#{}'.format(series_selector_id),first=True)
    options_list = series_selector.find('option')
    toggle = True
    for option in options_list:
        if toggle:
            toggle = False
            continue
        #print('link: {} name: {}'.format(option.attrs['value'],option.text))
        link = option.attrs['value']
        s_name = option.text
        print('Scanning: {}, {}'.format(br_name,s_name))
        build_pipeline(link,br_name,s_name)
        # print(link)

def build_pipeline(link,br_name,s_name):
    build_selector_id = 'build-selector'
    # session = HTMLSession()
    session = AsyncHTMLSession()
    response = session.get(link)
    total_requests = total_requests + 1
    total_scrapped_data = total_scrapped_data + len(response.html.html)
    html = response.html
    # html.render()
    build_selector = html.find('#{}'.format(build_selector_id),first=True)
    options_list = build_selector.find('option')
    toggle = True
    for option in options_list:
        if toggle:
            toggle = False
            continue
        #print('link: {} name: {}'.format(option.attrs['value'],option.text))
        link = option.attrs['value']
        bd_name = option.text
        print('Scanning: {}, {}, {}'.format(br_name,s_name,bd_name))
        specification_pipeline(link,br_name,s_name,bd_name)
        # print(link)


def specification_pipeline(link,br_name,s_name,bd_name):
    specification_selector_id = 'specification-selector'
    # session = HTMLSession()
    session = AsyncHTMLSession()
    response = session.get(link)
    total_requests = total_requests + 1
    total_scrapped_data = total_scrapped_data + len(response.html.html)
    html = response.html
    # html.render()
    specification_selector = html.find('#{}'.format(specification_selector_id),first=True)
    options_list = specification_selector.find('option')
    toggle = True
    for option in options_list:
        if toggle:
            toggle = False
            continue
        #print('link: {} name: {}'.format(option.attrs['value'],option.text))
        link = option.attrs['value']
        sp_name = option.text        
        print('Scanning: {}, {}, {}, {}'.format(br_name,s_name,bd_name,sp_name))
        table_pipeline(link,br_name,s_name,bd_name,sp_name)
        # print(link)


def table_pipeline(link,br_name,s_name,bd_name,sp_name):    
    try:
        # session = HTMLSession()
        session = AsyncHTMLSession()
        response = session.get(link)
        total_requests = total_requests + 1
        total_scrapped_data = total_scrapped_data + len(response.html.html)
        html = response.html
        # html.render()
        table = html.find('table',first=True)
        table_head = table.find('thead',first=True)
        th_list = table_head.find('th')
        # header = []
        # toggle = True
        # for th in th_list:
        #     if toggle:
        #         toggle = False
        #         continue
        #     print(th.text)
        #     header.append(th.text)
        table_body = table.find('tbody')
        data = []
        for tbody in table_body:
            row = []
            td_list = tbody.find('td')
            for td in td_list:
                # print(td.text)
                row.append(td.text)
            data.append(row)
    
        d_row = []
        for row in data:
            toggle = True
            for i in range(len(row)):
                if i != 0:
                    d_row.append(row[i])
    
        # for i in range(len(header)):
        #     for row in data:
        #         for j in range(1):
        #             print(header[i],row[0],row[i+1])
        csv_row = [br_name,s_name,bd_name,sp_name]
        csv_row = csv_row + d_row
        csv_writer.writerow(csv_row)
        print('write complete: ',csv_row)
    except Exception as e:
    	print('Exception Occures Causes: {}'.format(e))

try:
    brand_pipeline(site)
finally:
	print('Total Requests: {}'.format(total_requests))
	print('Total Scraped Data: {}'.format(total_scrapped_data))
    file.close()
