import win32com.client as com
 
APP_TYPE = 'Excel.Application'
 
xlBlack,xlRed,xlGray,xlBlue = 1,3,15,41
xlBreakFull = 1
 
 #初始化应用程序
xls = com.Dispatch(APP_TYPE)
xls.Visible = True
book = xls.Workbooks.Add()
sheet = book.Worksheets(1)
 
 #插入标题
ROW_PER_PAGE,COL_PER_ROW = 10, 10
row_index,col_index = 1,1
title_range = sheet.Range(sheet.Cells(row_index,col_index), sheet.Cells(row_index, COL_PER_ROW))
title_range.MergeCells = True
title_range.Font.Bold,title_range.Interior.ColorIndex = True,xlGray
title_range.Value = 'Hello,Word'
row_index += 1
 
 #插入内容 10*10的数列
for row in range(0, 10):
 col_index = 1
 for col in range(0, COL_PER_ROW):
  cell_range = sheet.Cells(row_index, col_index)
  cell_range.Font.Color,cell_range.Value = xlBlue,str(row)
 row_index += 1
 
 #插入分页符
#right_bottom_range = sheet.Cells(row_index, COL_PER_ROW+1)
#right_bottom_range.PageBreak = xlBreakFull
 
 #插入图片
col_index = 1
lt_range = sheet.Cells(row_index, col_index)
graph_width = sheet.Range(sheet.Cells(row_index,1), sheet.Cells(row_index, COL_PER_ROW)).Width
graph_height = sheet.Range(sheet.CellS(row_index,1), sheet.Cells(row_index+ROW_PER_PAGE, 1)).Height
sheet.Shapes.AddPicture('C:\\test.jpg', False, True, lt_range.Left, lt_range.Top, graph_width, graph_height)