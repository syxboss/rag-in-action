import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def test_nltk():
    # 测试文本
    text = "这是第一个句子。这是第二个句子！这是第三个句子？"
    
    print("测试NLTK功能:")
    print("-" * 50)
    
    # 测试句子分割
    print("\n1. 测试句子分割:")
    sentences = sent_tokenize(text)
    for i, sent in enumerate(sentences, 1):
        print(f"   句子{i}: {sent}")
    
    # 测试单词分割
    print("\n2. 测试单词分割:")
    words = word_tokenize(sentences[0])
    print(f"   分词结果: {words}")
    
    # 测试词性标注
    print("\n3. 测试词性标注:")
    english_text = "NLTK is working properly. This is a test sentence."
    words = word_tokenize(english_text)
    pos_tags = nltk.pos_tag(words)
    print(f"   词性标注结果: {pos_tags}")

if __name__ == "__main__":
    test_nltk() 