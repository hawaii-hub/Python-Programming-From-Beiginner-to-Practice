def make_shirt(size,text='I love Python'):
    """说明衬衫的尺码和字样"""
    print(f"\nThe t_shirt size is {size}.")
    print(f"The t_shirt text is {text}")

make_shirt(66,'niubi')
make_shirt(78,'jibal')

# 8.4 大号T恤
make_shirt('big')
make_shirt('medium')
make_shirt('small', 'I love China')