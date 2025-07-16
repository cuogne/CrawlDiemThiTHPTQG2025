from bs4 import BeautifulSoup
import requests
import json
    

urls = [f'https://diemthi.vnexpress.net/index/detail/sbd/5200307{i}/year/2025' for i in range(10)]

list_students = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sbd = url.split('sbd/')[1].split('/')[0] # get sbd
    diem = soup.find('tbody').text.strip().replace('\t', ' ').replace('\n', ' ').replace('  ', '')
    
    print(f'{sbd}: {diem}') # print test
    
    test = diem.split(' ')
    
    # strip score 
    scores = {}
    i = 0
    while i < len(test):
        # rule: find score (number) and extract subject name before it
        if test[i].replace('.', '').isdigit():
            score = float(test[i])

            subject_start = i - 1
            while subject_start >= 0 and test[subject_start] != '' and not test[subject_start].replace('.', '').isdigit():
                subject_start -= 1
            subject_start += 1
            
            if subject_start < i:
                subject = " ".join(test[subject_start:i])
                scores[subject] = score
            i += 1
        else:
            i += 1

    # create dict record for each student
    student_record = {
        'sbd': sbd,
        'scores': scores
    }
    
    # store it in the list
    list_students.append(student_record)

with open("list_students.json", 'w', encoding='utf-8') as f:
    json.dump(list_students, f, ensure_ascii=False, indent=2)

print(f"Saved scores for {len(list_students)} students to list_students.json")