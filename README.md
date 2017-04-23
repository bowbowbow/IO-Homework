# 비트코인 블록 분석

[![Build Status (Travis CI)][ci-svg]][ci]

[ci-svg]: https://api.travis-ci.org/earlbread/IO-Homework.svg
[ci]: https://travis-ci.org/earlbread/IO-Homework

비트코인 블록의 해쉬 값을 입력으로 받아 블록의 데이터를 출력합니다.

## 요구사항

- Python3

## 실행하기

커맨드라인에서 아래와 같이 실행합니다.

#### 블록 정보 출력

```bash
$ python3 blockinfo.py <hash_value>
```

각 출력 값 정보는 다음을 나타냅니다.

- Number of Transactions
    - 해당 블록의 트랜잭션 개수, 'n_tx'
- Average Value of Transactions
    - 각 트랜잭션의 'value' 값을 모두 더한 후 트랜잭션의 개수로 나눈 값으로 비트코인 최소 단위(1사토시)까지 표기
- Average Fee of Transactions
    - 해당 블록의 'fee'를 트랜잭션의 개수로 나눈 값으로 비트코인 최소 단위(1사토시)까지 표기
- Average Size of Transactions
    - 각 트랜잭션의 'size'를 모두 더한 후 트랜잭션의 개수로 나눈 값으로 int 형식으로 표기


#### 블록 내 트랜잭션의 Input 혹은 Output 정보 출력

```bash
$ python3 blockinfo.py <hash_value> <input | output>
```

각 출력 값 정보는 다음을 나타냅니다.

input
- hash : 각 트랜잭션의 hash 값
- inputs : 각 트랜잭션의 'inputs' 정보

output
- hash : 각 트랜잭션의 hash 값
- outputs : 각 트랜잭션의 'out' 정보


## 테스트하기

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ py.test
```
