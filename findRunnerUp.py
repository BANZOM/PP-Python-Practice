n = int(input())

#input for list separated by space
lst = list( map( int, input( ).split( ) ) )

print( max( i for i in lst if i != max(lst)))
