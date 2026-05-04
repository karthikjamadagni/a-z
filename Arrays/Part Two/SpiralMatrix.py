class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row = 0
        start_col = 0
        end_row = len(matrix) - 1
        end_col = len(matrix[0]) - 1

        return_list = []

        while (start_row <= end_row and start_col <= end_col):
            for j in range(start_col, end_col + 1):
                return_list.append(matrix[start_row][j])

            for i in range(start_row+1, end_row + 1):
                return_list.append(matrix[i][end_col])

            for j in range(end_col-1, start_col-1, -1):
                if start_row == end_row:
                    break
                return_list.append(matrix[end_row][j])

            for i in range(end_row-1, start_row, -1):
                if start_col == end_col:
                    break

                return_list.append(matrix[i][start_col])

            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1

        return return_list

        