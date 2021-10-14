# burden-tests-ProxECAT
VCF file preparation for ProxECAT rare variant burden test
VCF annotation - VEP for Python (havent tried other types)

UPD: \n
counting variant consequences in larger files (gnomad genomes, raw vcf, etc): better to use specialized Java tools, as Python is slow \n
https://pcingola.github.io/SnpEff/examples/ \n
command: \n
 java -Xmx8g -jar snpEff.jar -v -stats gnomad.html GRCh37.75 /mnt/home/controls/test.txt > out.txt   
