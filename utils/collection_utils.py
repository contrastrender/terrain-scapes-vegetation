def index_in_col(col, index):
    try:
        col[index]
        return True
    except:
        return False