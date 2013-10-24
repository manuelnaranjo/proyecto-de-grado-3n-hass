from ftplib import FTP

def pull(name, ftp):
    prg = open(name, 'wb')
    try:
        ftp.retrbinary('RETR %s' % name, prg.write)
        return True
    except:
        return False

def main():
    ftp = FTP('192.168.2.158')
    ftp.login()
    ftp.cwd('disk/prg')

    for i in ['plc_prg.pit', 'plc_err.pit', 'plc_msg.pit']:
        print i,
        print pull(i, ftp)
        
    ftp.quit()

if __name__=='__main__':
    main()
