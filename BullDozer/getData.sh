mkdir data;
cd data;
curl 'https://storage.googleapis.com/kaggle-data-sets/13827/18639/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1590730804&Signature=ZtHmOL23X7OH8pLPNugnmSqpPhYNt%2FJXS0fAu%2FDqbmhP3m2RneWr1PEwX%2FUBH5g1vmujI%2BWUdENhQP2izbD%2BQ2Qo5gnVEt32hgdTk5U7RcW3Md%2F6t8aGPZmnj4ZHG%2F47GBYzseJGD%2BX1KWMmCsxRjhJGT43BV6bKuw8ZbPjFlKqZfa2vezhpoUGlyEowwdCzcf7Yra9CejniHZwOU7VO5iyp%2B5mUmsnXUon6%2BNa4rHkZSylTF7tbMXiiN5a5RGxvSKdbkhxjwejrfoAV5YPoyIROx%2B5V4wNvH9XHmB2u2J4aecH7xO8Zt6htZ8wLpwH4GXarcRX3TdPcOp9RPfVN7Q%3D%3D&response-content-disposition=attachment%3B+filename%3Dblue-book-for-bulldozer.zip' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://www.kaggle.com/' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'TE: Trailers' -o data.zip;

unzip data.zip;

cd ..;
