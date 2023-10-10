import textstat
import emoji
from langdetect import detect

class TextAnalyzer:
    def __init__(self) -> None:
        pass
        
    def analyzeEn(self, main_text):
        textstat.set_lang("en")
        
        # Calculate readability scores
        flesch_reading_ease = textstat.flesch_reading_ease(main_text)
        flesch_kincaid_grade = textstat.flesch_kincaid_grade(main_text)
        gunning_fog = textstat.gunning_fog(main_text)
        smog_index = textstat.smog_index(main_text)
        coleman_liau_index = textstat.coleman_liau_index(main_text)
        standard_deviation = textstat.text_standard(main_text, float_output=False)
        
        # Calculate reading time
        reading_time = round(textstat.reading_time(main_text, ms_per_char=14.69) / 60, 1)
        
        easy_threshold = 70   
        hard_threshold = 30   
        
        def print_colored_score(score, label):
            if score >= easy_threshold:
                emoji_icon = emoji.emojize(":grinning_face_with_smiling_eyes:")   
                color_code = "\033[92m"  # Green
            elif score >= hard_threshold:
                emoji_icon = emoji.emojize(":neutral_face:")   
                color_code = "\033[93m"  # Yellow
            else:
                emoji_icon = emoji.emojize(":disappointed_face:")   
                color_code = "\033[91m"  # Red
            print(f"{label} {emoji_icon}: {color_code}{score}\033[0m")
        
        print_colored_score(flesch_reading_ease, "Flesch Reading Ease Score")
        
        def print_colored_grade_level(grade, label):
            if grade <= 6:
                emoji_icon = emoji.emojize(":grinning_face_with_smiling_eyes:")   
                color_code = "\033[92m"  # Green
            elif grade <= 12:
                emoji_icon = emoji.emojize(":neutral_face:")   
                color_code = "\033[93m"  # Yellow
            else:
                emoji_icon = emoji.emojize(":disappointed_face:")   
                color_code = "\033[91m"  # Red
            print(f"{label} {emoji_icon}: {color_code}{grade}\033[0m")
        
        print_colored_grade_level(flesch_kincaid_grade, "Flesch-Kincaid Grade")
        print_colored_grade_level(gunning_fog, "Gunning FOG Index")
        print_colored_grade_level(smog_index, "SMOG Index")
        print_colored_grade_level(coleman_liau_index, "Coleman-Liau Index")
        print("textstat Standard Deviation:", standard_deviation)
        print(f"Reading Time {emoji.emojize(':ten_o’clock:')} : {reading_time} Minutes")

    def analyzeDe(self, main_text):
        textstat.set_lang("de")
        
        # Calculate readability scores
        flesch_reading_ease = textstat.flesch_reading_ease(main_text)
        flesch_kincaid_grade = textstat.flesch_kincaid_grade(main_text)
        wiener_sachtextformel_1 = textstat.wiener_sachtextformel(main_text, 1)
        wiener_sachtextformel_2 = textstat.wiener_sachtextformel(main_text, 2)
        wiener_sachtextformel_3 = textstat.wiener_sachtextformel(main_text, 3)
        wiener_sachtextformel_4 = textstat.wiener_sachtextformel(main_text, 4)
        reading_time = round(textstat.reading_time(main_text, ms_per_char=14.69) / 60, 1)
        
        easy_threshold = 70  
        hard_threshold = 30  

        def print_colored_score(score, label):
            if score >= easy_threshold:
                emoji_icon = emoji.emojize(":grinning_face_with_smiling_eyes:")  
                color_code = "\033[92m"  # Green
            elif score >= hard_threshold:
                emoji_icon = emoji.emojize(":neutral_face:")  
                color_code = "\033[93m"  # Yellow
            else:
                emoji_icon = emoji.emojize(":disappointed_face:")  
                color_code = "\033[91m"  # Red
            print(f"{label} {emoji_icon}: {color_code}{score}\033[0m")
    
        print_colored_score(flesch_reading_ease, "Flesch Reading Ease Score")
        
        def print_colored_grade_level(grade, label):
            if grade <= 6:
                emoji_icon = emoji.emojize(":grinning_face_with_smiling_eyes:")  
                color_code = "\033[92m"  # Green
            elif grade <= 12:
                emoji_icon = emoji.emojize(":neutral_face:")  
                color_code = "\033[93m"  # Yellow
            else:
                emoji_icon = emoji.emojize(":disappointed_face:") 
                color_code = "\033[91m"  # Red
            print(f"{label} {emoji_icon}: {color_code}{grade}\033[0m")
    
        print_colored_grade_level(flesch_kincaid_grade, "Flesch-Kincaid Grade")
        print_colored_grade_level(wiener_sachtextformel_1, "Wiener Sachtextformel (1)")
        print_colored_grade_level(wiener_sachtextformel_2, "Wiener Sachtextformel (2)")
        print_colored_grade_level(wiener_sachtextformel_3, "Wiener Sachtextformel (3)")
        print_colored_grade_level(wiener_sachtextformel_4, "Wiener Sachtextformel (4)")
        print(f"Reading Time {emoji.emojize(':ten_o’clock:')} : {reading_time} Minutes")

    def analyzeAr(self, main_text):
        # Calculate the OSMAN Index for Arabic text
        osman_index = textstat.osman(main_text)
        
        easy_threshold = 70  
        hard_threshold = 30  
        
        def print_colored_osman_index(index):
            if index >= easy_threshold:
                emoji_icon = emoji.emojize(":grinning_face_with_smiling_eyes:")  
                color_code = "\033[92m"  # Green
            elif index >= hard_threshold:
                emoji_icon = emoji.emojize(":neutral_face:")   
                color_code = "\033[93m"  # Yellow
            else:
                emoji_icon = emoji.emojize(":disappointed_face:")   
                color_code = "\033[91m"  # Red
            print(f"OSMAN Index {emoji_icon}: {color_code}{index}\033[0m")
        
        print_colored_osman_index(osman_index)

    def analyze(self, main_text):
        lang = detect(main_text)
        if lang == "en":
            print("ENGLISH LANGUAGE DETECTED ",emoji.emojize(":United_Kingdom:") )
            self.analyzeEn(main_text)
        elif lang == "de":
            print("GERMAN LANGUAGE DETECTED ",emoji.emojize(":Germany:"))
            self.analyzeDe(main_text)
        elif lang == "ar":
            print("ARABIC LANGUAGE DETECTED ",emoji.emojize(":Egypt:"))
            self.analyzeAr(main_text)
        else:
            print(lang + " is NOT SUPPORTED")



f = open("tests/phd.txt", "r")
maintext = f.read()         
f.close()
tx = TextAnalyzer()
tx.analyze(maintext)