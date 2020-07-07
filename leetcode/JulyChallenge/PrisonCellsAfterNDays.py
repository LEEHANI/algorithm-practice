def prisonAfterNDays(cells, N):
    if N==0:
        return cells

    save_cells=[]
    for cnt in range(N):
        newCells=[0]
        for i in range(6):
            if cells[i]==cells[i+2]:
                newCells.append(1)
            else:
                newCells.append(0)
        newCells.append(0)

        cells=newCells
        if save_cells and save_cells[0]==cells:
            break

        save_cells.append(newCells)

    return save_cells[N%len(save_cells)-1]

print(prisonAfterNDays([0,1,0,1,1,0,0,1],7))
# print(prisonAfterNDays([1,0,0,1,0,0,1,0],1000000000))
# print(prisonAfterNDays([0,0,1,1,1,1,0,0],8))