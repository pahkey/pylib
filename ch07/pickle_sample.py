import pickle


def get_all_data():
    try:
        with open("data.p", 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


def add_data(no, subject, content):
    data = get_all_data()
    assert no not in data
    data[no] = {'no': no, 'subject': subject, 'content': content}
    with open('data.p', 'wb') as f:
        pickle.dump(data, f)


def get_data(no):
    data = get_all_data()
    return data[no]


# 데이터저장
add_data(1, '안녕 피클', '피클은 매우 간단합니다.')

# 데이터조회
data = get_data(1)
print(data['no'])
print(data['subject'])
print(data['content'])
