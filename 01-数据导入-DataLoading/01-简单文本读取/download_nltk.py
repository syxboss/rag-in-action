import nltk
import ssl
import sys
import os

def download_nltk_data():
    try:
        # 创建未验证的SSL上下文
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        # 设置NLTK数据目录
        nltk_data_dir = os.path.expanduser("~/nltk_data")
        if not os.path.exists(nltk_data_dir):
            os.makedirs(nltk_data_dir)
        
        # 设置下载路径
        nltk.data.path.append(nltk_data_dir)

        # 下载必要的NLTK数据包
        print("开始下载NLTK数据包...")
        packages = [
            'punkt',
            'punkt_tab',
            'averaged_perceptron_tagger',
            'averaged_perceptron_tagger_eng',  # 添加英语标注器
            'maxent_ne_chunker',
            'words',
            'perluniprops',  # 用于Unicode属性
            'universal_tagset',  # 通用标记集
            'nonbreaking_prefixes'  # 非断句前缀
        ]
        
        for package in packages:
            try:
                print(f"正在下载 {package}...")
                nltk.download(package, download_dir=nltk_data_dir, quiet=False)
                print(f"{package} 下载成功")
            except Exception as e:
                print(f"下载 {package} 时出错: {str(e)}")
                
        print("\n所有数据包下载完成")
        print(f"NLTK数据目录: {nltk.data.path}")
        
        # 验证关键包是否可用
        try:
            from nltk.tokenize import sent_tokenize
            from nltk.tag import pos_tag
            
            # 测试分句
            test_text = "This is a test sentence. This is another test sentence."
            sentences = sent_tokenize(test_text)
            
            # 测试词性标注
            words = nltk.word_tokenize(test_text)
            tags = pos_tag(words)
            
            print("\n验证测试成功！NLTK功能正常工作。")
            print(f"词性标注示例: {tags[:3]}")
            
        except Exception as e:
            print(f"\n验证测试失败: {str(e)}")
            sys.exit(1)
        
    except Exception as e:
        print(f"发生错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    download_nltk_data() 