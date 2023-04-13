import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

class ezWordCloud:
    def __init__(self, background_img_path: str, customize_stopword_path: str=None):
        """_summary_

        Parameters
        ----------
        background_img_path : str
            Using absolute path
        customize_stopword_path : str, optional
            Using absolute path
        """
        self.background_img_path = background_img_path
        self.customize_stopword_path = customize_stopword_path
    
    @property
    def img_mask(self):
        return np.array(Image.open(self.background_img_path))
    
    @property
    def __STOPWORDS(self):

        default_stopwords = set(STOPWORDS)
        with open(self.customize_stopword_path, '+r') as f:
            stopwords = f.readlines()
        
        stopwords = [sw.strip("\n") for sw in stopwords]
        
        for sw in stopwords:
            default_stopwords.add(sw)
        
        return default_stopwords
    
    def wc(self):
        wc = WordCloud(
            max_words=2000, 
            mask=self.img_mask,
            stopwords=self.__STOPWORDS, 
            contour_width=0,
            background_color=None,
            mode="RGBA"
        )
        return wc
    
    def generate(self, text_data: str, output_path: str):
        wc = self.wc()
        wc.generate(text_data)
        wc.to_file(output_path)

    def generate_from_frequency(self, text_data: str, output_path: str):
        wc = self.wc()
        freq = wc.process_text(text_data)
        wc.generate_from_frequencies(freq)
        wc.to_file(output_path)
