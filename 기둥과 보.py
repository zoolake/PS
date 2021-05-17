from collections import deque
def buildable(frames) -> bool:   
    for col, row, frame_type in frames:
        if frame_type == 0:
            if row == 0 or \
               (col, row, 1) in frames or \
               (col-1, row, 1) in frames or \
               (col, row-1, 0) in frames:
                continue
            else:
                return False
        else:              
            if (col, row-1, 0) in frames or \
               (col+1, row-1, 0) in frames or \
               ((col-1, row, 1) in frames and \
               (col+1, row, 1) in frames):
               continue
            else:
                return False
    return True

def solution(n, build_frame):
    frames = set()
    q = deque(build_frame)
    while q:
        col, row, frame_type, build = q.popleft()
        elem = (col, row, frame_type)

        if build:
            frames.add(elem)
            if not buildable(frames):
                frames.remove(elem)

        elif not build and elem in frames:
            frames.remove(elem)
            if not buildable(frames):
                frames.add(elem)

    answer = sorted(list(frames), key= lambda x: (x[0],x[1],x[2]))
    print(answer)
    return answer


