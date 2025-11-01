def moyenne(x):
    moyenne=sum(x)/len(x)
    return moyenne

def variance(x):
    moy=moyenne(x)
    var=1/len(x)*sum(x**2) - moy**2
    return var

def ecarts_type(x):
    return variance(x)**0.5

def covariance(x, y):
    moy_x=moyenne(x)
    moy_y=moyenne(y)
    cov=1/len(x)*sum(x*y) - moy_x*moy_y
    return cov

def correlation(x, y):
    cov=covariance(x, y)
    ecart_x=ecarts_type(x)
    ecart_y=ecarts_type(y)
    corr=cov/(ecart_x*ecart_y)
    return corr

def a_b(x, y):
    cov=covariance(x, y)
    var=variance(x)
    if var==0:
        raise ValueError("Variance of x is zero, cannot compute slope.")
    a=cov/var
    b=moyenne(y) - a*moyenne(x)
    return a, b