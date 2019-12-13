from get_features import FeatureMaker


def make_feature_file(fm):
    feature_file = open("feature_information.data", 'w')
    feature_file.write("classLast,{0},{1},space\n".format(fm.term_num(), fm.class_num()))
    for test_case_info in fm.case_info_list:
        str_vector = map(str, test_case_info.get_vector())
        feature_file.write("{0} {1}\n".format(" ".join(str_vector), test_case_info.get_classification()))
    feature_file.close()


if __name__ == '__main__':
    feature_maker = FeatureMaker()
    make_feature_file(feature_maker)
