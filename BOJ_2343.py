n, m = map(int, input().split())
lessons = list(map(int, input().split()))
left, right = max(lessons), sum(lessons)

while left <= right:
    mid = (left + right)//2
    disk = 0
    lesson_sum = 0

    for lesson in lessons:
        if lesson_sum + lesson > mid:
            disk += 1
            lesson_sum = 0
        lesson_sum += lesson
    if lesson_sum:
        disk += 1

    if disk <= m:
        right = mid - 1
    else:
        left = mid + 1

print(left)

