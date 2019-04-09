# IPSegmentScanner
:computer:Smarter network segment scanner! e.g. If you tell scanner to scan '192.0.1.1', it will be scan '192.0.1.1', '192.1.1.1', '192.2.1.1'... by your customize!

### Use Python 2.* plz!

### You must install "fping" to run this application!

#### For macOS:
```
brew install fping
```

#### For Linux:

```
apt-get install -y fping
```

or

```
yum install -y fping
```

# e.g.

If you want to scan segment C, Type:
python scanner.py -i 10.2.0.1 -r 0-20 -d -t 0

i - Specified IP address

r - Specified IP scan range

d - Show detials

t - Set timeout (Recommend 0 as second, if not working try 1)

You will got results:

```
Scanning 10.2.0-20.1
! 10.2.0.1
! 10.2.1.1
. 10.2.2.1
. 10.2.3.1
. 10.2.4.1
. 10.2.5.1
. 10.2.6.1
. 10.2.7.1
. 10.2.8.1
. 10.2.9.1
! 10.2.10.1
! 10.2.11.1
! 10.2.12.1
! 10.2.13.1
! 10.2.14.1
! 10.2.15.1
! 10.2.16.1
! 10.2.17.1
! 10.2.18.1
! 10.2.19.1
! 10.2.20.1

ALIVE HOSTS:
> 10.2.0.1
> 10.2.1.1
> 10.2.10.1
> 10.2.11.1
> 10.2.12.1
> 10.2.13.1
> 10.2.14.1
> 10.2.15.1
> 10.2.16.1
> 10.2.17.1
> 10.2.18.1
> 10.2.19.1
> 10.2.20.1
13 Online.
```
