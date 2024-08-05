import pytest


def test_search_element_js_script_contain():
    js_contain_test = """
            var spanElements = document.evaluate("//span[contains(text(), 'Войти')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
            return spanElements.singleNodeValue;
    """
    tag = 'span'
    params = None
    contain_text = 'Войти'
    js_contain_sample = f"""
            var spanElements = document.evaluate("//{tag}[contains(text(), '{contain_text}')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
            return spanElements.singleNodeValue;
    """
    assert js_contain_sample == js_contain_test

def test_search_element_js_script_params():
    js_params_test = """
                var inputElement = document.evaluate("//iframe[@id='authFrame']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                return inputElement.singleNodeValue;
    """
    tag = 'iframe'
    params = {'id': 'authFrame'}
    contain_text = None
    tags_list = [f'@{x}' for x in params.keys()]
    names_list = [f"'{x}'" for x in params.values()]
    params_list= []
    for x, y in zip(tags_list, names_list):
        params_list.append(f'{x}=')
        params_list.append(f'{y}, ')
    params_string = ''.join(params_list)[:-2]
    params_string = '['+params_string+']'
    js_params_sample = f"""
                var inputElement = document.evaluate("//{tag}{params_string}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                return inputElement.singleNodeValue;
    """
    assert js_params_test == js_params_sample

def test_search_element_no_params():
    js_test = """
                    var inputElement = document.evaluate("//iframe", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                    return inputElement.singleNodeValue;
    """
    tag = 'iframe'
    params_string = None
    js_sample = f"""
                    var inputElement = document.evaluate("//{tag}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                    return inputElement.singleNodeValue;
    """
    print(js_sample)
    assert js_test == js_sample