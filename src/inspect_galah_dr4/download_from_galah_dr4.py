import wget

def download_galah_dr4_allstar(target_directory = './'):
	url = 'https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/galah_dr4_allstar_placeholder.fits'
	wget.download(url,target_directory)

if __name__ == '__main__':
    download_galah_dr4_allstar()
