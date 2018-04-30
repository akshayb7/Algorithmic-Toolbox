# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
	""" 
	Function functionality:
	Given a set of n segments with integer coordinates on a line, find
	the minimum number of points such that each segment contains at least one point.
	"""
	points = []
	#Sort the segments by their right end points (x.end)
	sort_seg = sorted(segments, key=lambda x: x.end)
	
	while sort_seg:
		current_segment = sort_seg.pop(0)
		#Take the right end point of segment as a point
		point = current_segment.end 
		points.append(point)
		#Check other segments for the current point and remove if it hits
		for i in sort_seg[:]:
			if i.start <= point and point <= i.end:
				sort_seg.remove(i)
	
	return points			

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *data = map(int, input.split())
	segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
	points = optimal_points(segments)
	print(len(points))
	for p in points:
		print(p, end=' ')
