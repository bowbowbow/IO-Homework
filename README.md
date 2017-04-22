# 비트코인 블록 분석

비트코인 블록의 해쉬 값을 입력으로 받아 블록의 데이터를 출력합니다.

## 요구사항

- Python3

## 실행하기

커맨드라인에서 아래와 같이 실행합니다.

블록 정보 출력

```bash
$ python3 blockinfo.py <hash_value>
```

블록 내 트랜잭션의 Input 혹은 Output 정보 출력

```bash
$ python3 blockinfo.py <hash_value> <input | output>
```


## 테스트하기

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ py.test
```
