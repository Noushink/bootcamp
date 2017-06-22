def ecdf(data):

    x = np.sort(data)
    y = np.arange (1, len(data)+1)/len(data)
    return x, y

xa_high = np.loadtxt ('', comments='#')
xa_low = np.loadtxt('', comments='#')

x_high, y_high = ecdf()
x_low, y_low = ecdf()
