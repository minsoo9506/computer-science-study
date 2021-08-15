# 출처 : https://www.daleseo.com/python-asyncio/

# 동기 프로그래밍
import time

def find_users_sync(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번째 사용자 조회 중 ...')
        time.sleep(1)
    print(f'> 총 {n} 명 동기 조회 완료!')

def process_sync():
    start = time.time()
    find_users_sync(3)
    find_users_sync(2)
    find_users_sync(1)
    end = time.time()
    print(f'>>> 동기 처리 총 소요 시간: {end - start}')

# 비동기 프로그래밍
# 기존 함수 선언에 async 키워드를 불여서 비동기함수(코루틴)으로 변경
# 비동기함수 호출시 await 키워드 붙임

import asyncio

async def find_users_async(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번째 사용자 조회 중...')
        await asyncio.sleep(1) # 그냥 1초 쉬는게 x 다른 처리 진행
    print(f'> 총 {n} 명 비동기 조회 완료!')

async def process_async():
    start = time.time()
    await asyncio.wait([
        find_users_async(3),
        find_users_async(2),
        find_users_async(1)
    ])
    end = time.time()
    print(f'>>> 비동기 처리 총 소요 시간: {end - start}')


if __name__ == '__main__':
    process_sync() # 6초 걸린다
    print('---------------------------')
    asyncio.run(process_async()) #3초