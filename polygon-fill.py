class Image:

  def __init__(self,filename):
    self.m = []
    self.setData(filename)
    self.boundary = []
    
  
  def setData(self,filename):
    with open(filename) as f:
      # first line is the image size length and width:
      firstLine = f.readline()
      size = firstLine.split()
      self.rows = int(size[0])
      self.cols = int(size[1])
      # second line is the boder/polygon color
      self.poly = int(f.readline().split()[0])
      # third line is the fill color
      self.fill = int(f.readline().split()[0])
      # fourth line is the target coordinate
      firstLine = f.readline()
      target = firstLine.split()
      self.x = int(target[0])
      self.y = int(target[1]) 
      # the rest is the matrix
      for row in range(self.rows):
        matrix_row = f.readline().split()
        self.m.append([int(item) for item in matrix_row])

  def isInnerPoint(self,x,y):
    # invalid/out of bounds input
    if (x < 0 or x >= self.rows) or (y < 0 or y >= self.cols):
      return
    # get the scan line
    scan = list(self.m[x])
    # get intersections of polygon and scan line
    sections = []
    for i in range(len(scan)):
      if scan[i] == self.poly:
        sections.append(i)
    # return False if no intersections
    if len(scan) == 0:
      return False
    # alternating flag for non-contiguous intersections
    flag = False
    for index in range(len(scan)):
      if index in sections and index+1 not in sections:
        flag = not flag
      if flag and index == y:
        return True
      



  def color(self, x, y):
    if not self.isInnerPoint(x,y):
      return
    elif self.m[x][y] == self.poly or self.m[x][y] == self.fill:
      return
    else:
      self.m[x][y] = self.fill
      if x+1 < self.rows:
        self.color(x+1,y)
      if x-1 >= 0:
        self.color(x-1,y)
      if y+1 < self.cols:
        self.color(x,y+1)
      if y-1 >= 0:
        self.color(x,y-1)

    




  def __repr__(self):
    s = ''
    for row in self.m:
      for item in row:
        s += str(item)
        s += '\t'
      s += '\n'
    return s


# for test:

im1 = Image('poly1.txt')
im2 = Image('poly2.txt')
im3 = Image('poly3.txt')
im1.color(5,5)
im2.color(1,1)
im3.color(1,9)

print(im1)
print(im2)
print(im3)