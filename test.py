import time
import ClassJsonMapper


start = time.time()
with ClassJsonMapper.Mapper("test.json") as mapper:
    # print(mapper.read())
    # print(mapper.get("name"))
    # print(mapper.get("age"))
    # print(mapper.get("dict"))
    # print(mapper.get("dict.1"))
    # print(mapper.get("list"))
    # print(mapper.get("list.0"))
    # print(mapper.get("list.[0:2]"))
    # print(mapper.get("list")[0:2])
    print(mapper.set("age", 19))
    print(mapper.set("dict.1", "Python"))
    print(mapper.set("list.6.0.1", "Python!"))
    print(mapper.set("list.6.0.2", "Python!"))

    # print(mapper.get("wapPopAdvert.url"))
    # print(mapper.get("wapPopAdvert.background"))
    # print(mapper.get("topicData"))

    mapper.write()
end = time.time()
print(f"耗时: {end - start}")