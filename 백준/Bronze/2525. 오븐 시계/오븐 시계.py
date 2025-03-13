hour, minute = map(int, input().split())
times = int(input())

# 지나간 시간 중 시간 단위 계산 ( times(분) // 60 )
time_hour = times // 60
# 지나간 시간 중 분 단위 계산 ( times(분) - (지나간 시간 * 60) )
time_minute = times - (time_hour * 60)

# 지나간 시간과 분 적용
hour += time_hour
minute += time_minute

# 초과된 시간 계산
hour = (hour + (minute // 60)) % 24
minute = minute % 60

print(hour, minute)