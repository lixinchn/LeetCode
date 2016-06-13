class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @staticmethod
    def create(arrs):
        intervals = []
        for arr in arrs:
            interval = Interval(arr[0], arr[1])
            intervals.append(interval)
        return intervals


class Solution(object):
    def adjust_left(self, box, middle):
        index = middle - 1
        interval = box[middle]
        while True:
            if index < 0:
                break
            target_interval = box[index]
            if target_interval.end < interval.start:
                break
            if target_interval.start < interval.start:
                interval.start = target_interval.start 
            box.remove(target_interval)
            index -= 1
            middle -= 1
        return middle

    def adjust_right(self, box, middle):
        index = middle + 1
        interval = box[middle]
        while True:
            if index >= len(box):
                break
            target_interval = box[index]
            if target_interval.start > interval.end:
                break
            if target_interval.end > interval.end:
                interval.end = target_interval.end
            box.remove(target_interval)
            # index += 1

    def insert(self, box, interval):
        len_box = len(box)
        left, right = 0, len_box - 1
        while True:
            if left >= len_box:
                box.append(interval)
                break
            if right < 0:
                box.insert(0, interval)
                break
            if left > right:
                box.insert(left, interval)
                break

            middle = (left + right) / 2
            temp_interval = box[middle]
            if temp_interval.start > interval.end:
                right = middle - 1
                continue
            if temp_interval.end < interval.start:
                left = middle + 1
                continue
            if temp_interval.start >= interval.start and temp_interval.end <= interval.end:
                temp_interval.start = interval.start
                temp_interval.end = interval.end
                middle = self.adjust_left(box, middle)
                self.adjust_right(box, middle)
                break
            if temp_interval.start <= interval.end and temp_interval.start > interval.start:
                temp_interval.start = interval.start
                self.adjust_left(box, middle)
                break
            if temp_interval.start <= interval.start and temp_interval.end >= interval.end:
                break
            if temp_interval.end >= interval.start and temp_interval.end < interval.end:
                temp_interval.end = interval.end
                self.adjust_right(box, middle)
                break


    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals

        box = []
        for interval in intervals:
            if interval.start > interval.end:
                continue
            self.insert(box, interval)
        return box

if __name__ == "__main__":
    solution = Solution()
    intervals = Interval.create([[2,3],[4,5],[6,7],[8,9],[1,10]])
    ret = solution.merge(intervals)
    for value in ret:
        print 'start: %s, end: %s' % (value.start, value.end)

    # intervals = Interval.create([[1,3],[2,6],[8,10],[15,18]])
    # ret = solution.merge(intervals)
    # for value in ret:
    #     print 'start: %s, end: %s' % (value.start, value.end)

    # intervals = Interval.create([[5,7],[0,0],[2,2],[3,3],[4,4],[3,5]])
    # ret = solution.merge(intervals)
    # for value in ret:
    #     print 'start: %s, end: %s' % (value.start, value.end)

    # intervals = Interval.create([[1,4],[0,5]])
    # ret = solution.merge(intervals)
    # for value in ret:
    #     print 'start: %s, end: %s' % (value.start, value.end)

    # intervals = Interval.create([[1,4],[0,0]])
    # ret = solution.merge(intervals)
    # for value in ret:
    #     print 'start: %s, end: %s' % (value.start, value.end)

    # intervals = Interval.create([[374,383],[314,319],[441,446],[268,275],[466,470],[232,238],[284,292],[383,390],[356,361],[365,368],[327,330],[122,131],[149,153],[258,265],[343,350],[472,481],[17,25],[85,85],[16,21],[399,401],[79,81],[360,365],[250,253],[34,42],[150,159],[53,62],[14,20],[29,32],[310,319],[73,79],[347,354],[427,433],[36,40],[378,380],[70,78],[34,43],[410,414],[217,217],[489,490],[470,479],[3,7],[468,477],[52,61],[385,387],[341,349],[220,228],[355,355],[256,257],[364,368],[295,299],[412,421],[436,440],[75,80],[186,190],[108,115],[55,56],[181,185],[333,336],[225,233],[447,453],[176,176],[106,109],[372,374],[127,133],[349,351],[23,26],[104,105],[288,297],[168,174],[96,102],[483,484],[240,246],[175,178],[101,102],[143,144],[319,320],[273,279],[54,61],[140,141],[85,94],[104,112],[455,455],[271,274],[239,240],[421,426],[420,427],[487,487],[273,277],[85,92],[267,267],[480,489],[251,256],[365,370],[102,107],[339,346],[495,500],[148,148],[355,356],[45,49],[63,71],[282,285],[75,76],[495,504],[487,489],[428,435]])
    # ret = solution.merge(intervals)
    # for value in ret:
    #     print 'start: %s, end: %s' % (value.start, value.end)

