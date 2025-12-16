def data_types():
    var_int = 42
    var_str = "Hello, World!"
    var_float = 3.14
    var_bool = True
    var_list = [1, 2, 3, 4, 5]
    var_dict = {"name": "John", "age": 30}
    var_tuple = (1, 2, 3)
    var_set = {1, 2, 3, 4}
    types_list = [
        type(var_int).__name__,
        type(var_str).__name__,
        type(var_float).__name__,
        type(var_bool).__name__,
        type(var_list).__name__,
        type(var_dict).__name__,
        type(var_tuple).__name__,
        type(var_set).__name__
    ]
    
    print(types_list)

if __name__ == '__main__':
    data_types()