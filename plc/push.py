from ftplib import FTP

def push(name, ftp):
    prg = open(name)
    try:
        ftp.storbinary('STOR %s' % name, prg)
        return True
    except:
        return False

def main():
    ftp = FTP('192.168.2.158')
    #ftp.set_debuglevel(3)
    ftp.login()

    ftp.voidcmd('TYPE I')
    ftp.cwd('disk/prg')

    for i in ['plc_prg.pit', 'plc_err.pit', 'plc_msg.pit']:
        print i,
        print push(i, ftp)

    ftp.quit()

if __name__=='__main__':
    main()
