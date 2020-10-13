'''
Created on Oct 9, 2020

@author: mukund
'''
import baseclass
import pageUIelement
import constantfile

class AssertDynamicText(baseclass.BaseClass):

    def findTextCharLength(self, textValue):
        splitText = textValue.split()
        for eachString in splitText:
            if len(eachString) >= 10:
                return True
        return False

    def findLongestString(self,longestString):
        compareString = ''
        splitText = longestString.split()
        for eachString in splitText:
            if len(eachString) > len(compareString):
                compareString = eachString
        return compareString

    def test_assertDynamicTextInWebPage(self):
        self.driver.implicitly_wait(1000)
        finalLongestString = ''

        dText1 = self.driver.find_element_by_css_selector(pageUIelement.PageUIElements.first_dynamicText)
        resultValue = self.findTextCharLength(dText1.get_property('innerText'))
        longestString = self.findLongestString(dText1.get_property('innerText'))
        self.assertEqual(resultValue, True, "The Dynamic Text in the page has atLeast 10 Character long.")

        dText2 = self.driver.find_element_by_css_selector(pageUIelement.PageUIElements.second_dynamicText)
        resultValue = self.findTextCharLength(dText2.get_property('innerText'))
        longestString2 = self.findLongestString(dText1.get_property('innerText'))

        if len(longestString) > len(longestString2):
            self.finalLongestString = longestString
        else:
            finalLongestString = longestString2
        self.assertEqual(resultValue, True, "The Dynamic Text in the page has atLeast 10 Character long.")

        dText3 = self.driver.find_element_by_css_selector(pageUIelement.PageUIElements.Third_dynamicText)
        resultValue = self.findTextCharLength(dText3.get_property('innerText'))
        longestString3 = self.findLongestString(dText1.get_property('innerText'))
        if len(finalLongestString) < len(longestString3):
            self.finalLongestString = longestString3
        print('Longest String appeared in the page:', finalLongestString)
        self.assertEqual(resultValue,True, "The Dynamic Text in the page has atLeast 10 Character long.")

    def test_assertDynamicTextInWebPage(self):
        img_list = []
        self.driver.implicitly_wait(1000)
        img1 = self.driver.find_element_by_css_selector(pageUIelement.PageUIElements.image_avatar1)
        pic = img1.get_property('src')
        img2 = self.driver.find_element_by_css_selector(pageUIelement.PageUIElements.image_avatar2)
        pic1 = img2.get_property('src')
        img3 = self.driver.find_element_by_css_selector(pageUIelement.PageUIElements.image_avatar3)
        pic2 = img3.get_property('src')
        img_list.append(pic)
        img_list.append(pic1)
        img_list.append(pic2)

        for eachImg in img_list:
            if eachImg == constantfile.ConstantFile.image_punisher:
                flag = True
                break
            else:
                flag = False
        self.assertEqual(flag, True, "Punisher image is not present")

