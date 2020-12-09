with open("C:\\Users\\dedwards\\projects\\2020-Advent\\Day 05\\seats.dat") as seatData:
    seats = seatData.read().split('\n')

highestSeatID=0
takenSeats=[]

for seat in seats:
    rowStr=seat[0:7]
    colStr=seat[7:10]
    rowBin=rowStr.replace('B','1').replace('F','0')
    colBin=colStr.replace('R','1').replace('L','0')
    rowDec=int(rowBin, 2)
    colDec=int(colBin, 2)
    seatId=rowDec*8+colDec
    takenSeats.append(seatId)

takenSeats.sort()
allSeats=list(range(int(takenSeats[0]),int(takenSeats[-1])))
ourSeat=list(set(allSeats)-set(takenSeats))

print('Our Seat: {}'.format(ourSeat))
