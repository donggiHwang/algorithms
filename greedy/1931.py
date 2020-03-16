"""
이 문제는 최대한 많은 회의를 집어넣어야 하므로, 일찍 끝나는 회의부터 집어넣어,
회의가 끝난 후에 다른 회의가 이어질 수 있도록 해야하는 문제이다.
그러므로, 우선 전체 회의 목록을 종료시간 순서로 정렬을 하고, 마지막 회의가 끝난
시간을 기록하여 다음 회의를 계획할 수 있도록 한다. 여기서, 시작과 종료 시간이
같은 회의가 먼저 들어가면, 이 회의와 종료 시간이 같지만 먼저 시작하여,
회의실을 사용할 수 있는 다른 회의가 들어가지 못하는 경우가 생길 수 있다.
그러므로, 종료 시간으로 정렬한 후에, 시작 시간으로 다시 정렬하여 이러한 문제를
방지한다.
"""
numOfMeeting = int(input())
meetingList = []
for i in range(0, numOfMeeting):
    timeOfMeeting = [int(i) for i in input().split(' ')]
    meetingList.append(timeOfMeeting)
meetingList.sort(key=lambda x: (x[1], x[0]))
startTime = 0
meetingCount = 0
for i in meetingList:
    if i[0] >= startTime:
        meetingCount += 1
        startTime = i[1]
print(meetingCount)
