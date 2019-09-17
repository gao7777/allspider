import json

def main():
    with open("/home/gaozhiwei/Desktop/javatest.json",) as f:
        json_data = f.read()


    data = json.loads(json_data)
    print(data)
    final_dict=dict()
    final_dict['dict'] = []
    for i in data['dict']:
        print(i)
        values = i['value']
        print(values)
        i['value'] = list(set(values))
        final_dict['dict'].append(i)
    with open("/home/gaozhiwei/Desktop/contentname_sort_uniq720dierban.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))













if __name__ == '__main__':
    main()