with open("seats.dat") as seatData:
    seats = seatData.read().split('\n')

highestSeatID=0

for seat in seats:
    rowStr=seat[0:7]
    colStr=seat[7:10]
    rowBin=rowStr.replace('B','1').replace('F','0')
    colBin=colStr.replace('R','1').replace('L','0')
    rowDec=int(rowBin, 2)
    colDec=int(colBin, 2)
    seatId=rowDec*8+colDec
    print('Seat: {} row: {} col: {} rowBin: {} colBin: {} rowDec: {} colDec: {} seatId: {}'.format(seat, rowStr, colStr, rowBin, colBin, rowDec, colDec, seatId))
    if(seatId > highestSeatID):
        highestSeatID=seatId

print('Highest SeatId: {}'.format(highestSeatID))
