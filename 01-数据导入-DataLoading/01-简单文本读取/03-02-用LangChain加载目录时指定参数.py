from langchain_community.document_loaders import DirectoryLoader
loader = DirectoryLoader("90-文档-Data/黑悟空", 
                        glob="**/*.md", 
                        use_multithreading=True,
                        show_progress=True,
                        )
docs = loader.load()
print(f"文档数：{len(docs)}")  # 输出文档总数
print(docs[0])  # 输出第一个文档