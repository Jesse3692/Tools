# Functional code snippet

## Python

### 1. 内置数据类型

#### 1.1 字符串

1. [字符串格式化](https://github.com/Jesse3692/tools/blob/master/docs/字符串格式化.md)
   - C语言的方式`%`
   - format()
   - f-string
2. 字符串的拼接

#### 1.2 数字

1. 数字格式化

   ```python
   In [1]: pi = 3.141592654
   
   In [2]: print('pi is %.4f' % (pi,))
   pi is 3.1416
   
   In [3]: print('pi is {:.4f}'.format(pi))
   pi is 3.1416
   ```

   

### . [文件操作](https://github.com/Jesse3692/Tools/blob/master/sourcecode/file/文件操作.md)

#### 大文件读取

#### excel文件的读写

```python
import openpyxl

def write_to_xlsx(path, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
    workbook.save(path)
    print("xlsx表格成功写入数据")

def read_to_xlsx(path, sheet_name):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet_name]
    for row in sheet.rows:
        for cell in row:
            print(cell.value, "\t", end="")
        print()
```

[详细代码](https://github.com/Jesse3692/Tools/blob/master/sourcecode/file/operate_excel.py)

### . 日志操作

### . 加密操作

### . 代码测试

### . 底层相关

## CSS