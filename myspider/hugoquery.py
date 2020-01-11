import os
import time
from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED, wait

import requests

all_merchandid = {"81": ["2609509842712408242", "7501012293520623844", "2552481800851264227", "2609509842712408242",
                         "7501012293520623844", "2552481800851264227", "2609509842712408242", "7501012293520623844"],
                  # "minipod_plus":["6744752193241616162"],
                  "155": ["7539408370864904354"],
                  # "minipod":["6640321023923275438", "3112614791830744643"],
                  "45": ["4563703254633251759", "6791176275608079900", "3163684076898702361", "2609509842712408242",
                         "4073660508957432976", "7501012293520623844", "4557700610173426351", "1285635473410178445",
                         "2400847406295678798", "7522291502751657193", "7539408370864904354", "8632975314087256938",
                         "6172934047989787860", "3754990154023337689", "8452162142175285303", "8329586054827698712",
                         "7727005201896400679", "7621901819492589897", "2552481800851264227", "2326020018098260793",
                         "6744752193241616162", "2527525047308931735", "6290140341897714379", "8832091840866486980",
                         "6172934047989787860", "3754990154023337689", "8832091840866486980", "7539408370864904354",
                         "7727005201896400679"],
                  # "music_sai": ["6640321023923275438", "3112614791830744643"],
                  # "letu":["2527525047308931735"],
                  "17": ["2609509842712408242", "7501012293520623844", "2552481800851264227", ]}


def hugo_post(query, merchantid):
    header = {'Content-Type': 'application/json'}

    body = {
        "merchantId": "154",
        "clientId": "888101",
        "dialogId": 666101,
        "query": "老虎叫声",
        "deviceId": "wangle"
    }
    url = "http://k8s-m.sai.corp:31001/hugo/semantic/v2"
    # url = "http://k8s-m.sai.corp:31001/hugo/semantic/v3?app_id=154"

    for key, value in all_merchandid.items():
        # print(key,value)
        if merchantid in value:
            # print(key)
            body.update({'query': query, 'merchantId': key})
            break
    else:
        body.update({'query': query, 'merchantId': merchantid})
    # print(body)
    time.sleep(0.3)
    res = requests.post(url=url, json=body)
    print(query, merchantid)
    print(res.text)


def main():
    # base_path = '/home/gaozhiwei/Desktop/svk91-98log/'
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'svk91-98log')
    # print(base_path)

    file_names_list = os.listdir(base_path)
    executer = ThreadPoolExecutor(max_workers=2)
    all_task = list()
    for filename in file_names_list:
        with open(os.path.join(base_path,filename)) as f:
            data_list = f.readlines()
        for query in data_list:
            cur_list = query.strip().split(',')
            mechantid = cur_list[3]
            query = cur_list[2]
            # task = executer.submit(hugo_post(query, mechantid))
            # all_task.append(task)
    wait(all_task, return_when=ALL_COMPLETED)


if __name__ == '__main__':
    main()
