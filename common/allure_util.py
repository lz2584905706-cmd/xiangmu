import allure

def set_allure_info(case):
    title = case.get("case_name","未命名测试用例").format(**case)
    feature = str(case.get("feature") or "").strip()
    story = str(case.get("story") or "").strip()

    allure.dynamic.title(title)
    if feature:
        allure.dynamic.feature(feature)
    if story:
        allure.dynamic.story(story)
