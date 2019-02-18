import requests
import json
import os

class Spider:
    def __init__(self):
        self.session = requests.Session()

    def run(self,word):
        self.search(word)

    def search(self,word):
        url = 'http://fanyi.baidu.com/v2transapi'
        data = {
            'from' : 'en',
            'to' : 'zh',
            'query' : word,
            'transtype' : 'realtime',
            'simple_means_flag' :  3
        }
        response = self.session.post(url,data)
        info = json.loads(response.text)['dict_result']['simple_means']['symbols'][0]
        # print(info)
        save_info = [word]
        save_info.append('英 [%s] 美 [%s]' % (info['ph_en'],info['ph_am']))
        for part in info['parts']:
            save_info.append("%s%s" % (part['part'],';'.join(part['means'])))
            print(save_info)
            save_info = ['%s\n' % x for x in save_info]
            uk_url = 'http://fanyi.baidu.com/getts?lan=uk&text=%s&spd=3&source=web' % word
            en_url = 'http://fanyi.baidu.com/getts?lan=en&text=%s&spd=3&source=web' % word
            uk_mp3 = self.session.get(url).content
            en_mp3 = self.session.get(url).content
            self.save(save_info,word,en_mp3,uk_mp3)

    def save(self,save_info,word,en_mp3,uk_mp3):
        if not os.path.exists(word):
            os.makedirs(word)
            file_path = os.path.join(word,"%s.txt"% word)
            print(file_path)
            with open(file_path,'w',encoding='utf-8') as f:
                f.writelines(save_info)
            uk_path = os.path.join(word, '%suk.mp3' % word)
            en_path = os.path.join(word, '%suk.mp3' % word)
            with open(uk_path,'wb') as f:
                f.write(uk_mp3)
            with open(uk_path,'wb') as f:
                f.write(en_mp3)


if __name__ == '__main__':
    spider = Spider()
    spider.run('find')
