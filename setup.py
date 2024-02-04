from setuptools import setup, find_packages

# 项目元数据
metadata = {
    'name': 'YourProjectName',  # 项目名称
    'version': '1.0.0',         # 版本号
    'description': 'A short description of your project.',  # 简短描述
    'long_description': open('README.md', encoding='utf-8').read(),  # 可以读取 README 文件内容作为详细描述
    'long_description_content_type': 'text/markdown',  # 如果使用 Markdown 格式的 README
    'author': 'Your Name',      # 作者姓名
    'author_email': 'your.email@example.com',   # 作者邮箱
    'url': 'https://github.com/yourusername/YourProjectName',  # 项目主页
    'license': 'MIT',           # 许可证类型
    'classifiers': [            # 类别列表，用于PyPI展示
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    'keywords': ['keyword1', 'keyword2'],  # 关键字列表
    'packages': find_packages(exclude=['tests', 'docs']),  # 自动查找包含__init__.py的子目录作为包
    'install_requires': [          # 项目依赖项列表
        'dependency1 >= 1.0.0',
        'dependency2 ~= 2.5',
    ],
    'extras_require': {            # 可选依赖项
        'dev': [
            'pytest>=6.0',
            'flake8',
        ],
        'docs': [
            'sphinx',
            'recommonmark',
        ],
    },
}

# 执行 setup 函数来定义项目结构和生成所需的打包命令
setup(**metadata)