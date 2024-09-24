import math
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
import torch.nn as nn
def get_feature(column, data):
    '''
    :param column: 需要读取的excel列
    :param data: excel表格数据
    :return:
    '''
    feature = []

    # 定义获取某一列的时域特征的函数，输入为一维的Dataframe格式的数据
    def get_time_domain_features(data):
        '''data为一维振动信号'''
        fea = []
        len_ = len(data)
        mean_ = data.mean()  # 1.均值
        var_ = data.var()  # 2.方差
        std_ = data.std()  # 3.标准差
        max_ = data.max()  # 4.最大值
        min_ = data.min()  # 5.最小值
        x_p = max(abs(max_), abs(min_))  # 峰值
        x_rms = math.sqrt((data ** 2).sum() / len_)  # 均方根值
        x_r = ((abs(data) ** 0.5).sum() / len_) ** 2  # 方根幅值
        W = x_rms / mean_  # 波形指标
        C = x_p / x_rms  # 峰值指标
        I = x_p / mean_  # 脉冲指标
        L = x_p / x_r  # 裕度指标
        S = ((data - mean_) ** 3).sum() / ((len_ - 1) * std_ ** 3)  # 偏斜度
        K = ((data - mean_) ** 4).sum() / ((len_ - 1) * std_ ** 4)  # 峭度
        fea = [mean_, var_, std_, max_, min_, x_p, x_rms, x_r, W, C, I, L, S, K]
        return fea

    for i in column:
        feature.append(get_time_domain_features(data[i]))
    feature = np.concatenate(feature, axis=0)
    return feature.reshape(1, -1)

class MinMaxScaler:
    def __init__(self, feature_range=(0, 1)):
        self.feature_range = feature_range
        self.data_min_ = np.array([2.08181891e+01 , 1.94223871e+02,  1.39364225e+01 , 4.77228319e+01,
                                  7.39843611e+00 , 4.77228319e+01 , 2.97357981e+01 , 1.66282375e+01,
                                  1.07198845e+00 , 1.60318257e+00 , 1.81402549e+00 , 1.94767880e+00,
                                  4.72060198e-01 , 1.55429913e+00 , 5.70014993e+03 , 6.26230532e+06,
                                  2.50245985e+03 , 8.00000000e+03 ,-2.42432137e+01 , 8.00000000e+03,
                                  6.28365338e+03 , 5.22394845e+03 , 1.05218692e+00 , 1.17493568e+00,
                                  1.26086957e+00,  1.34644361e+00, -1.21392738e+00 , 1.49933569e+00,
                                  5.19241311e+01 , 4.90081331e+01,  7.00058092e+00 , 7.62535332e+01,
                                  4.16596591e+01 , 7.62535332e+01,  5.39623998e+01 , 5.10320994e+01,
                                  1.00453276e+00 , 1.29529471e+00 , 1.31617190e+00 , 1.32647981e+00,
                                  1.19631934e-01 , 1.91876141e+00 , 2.32256108e+01 , 2.72664376e+01,
                                  5.22172745e+00 , 3.43886910e+01, -8.43661539e+00 , 3.43886910e+01,
                                  2.69886165e+01 , 1.97057589e+01,  1.01288375e+00,  1.07336255e+00,
                                  1.11372229e+00 , 1.12293161e+00 ,-2.45454463e+00 , 1.67688019e+00,
                                  4.16651038e+00 , 3.11589252e-04 , 1.76518909e-02 , 4.20277778e+00,
                                  2.76388889e+00 , 4.20277778e+00 , 4.16654774e+00 , 4.16649168e+00,
                                  1.00000014e+00 , 1.00106981e+00 , 1.00106994e+00 , 1.00107001e+00,
                                 -2.63868147e-01 , 1.83138161e+00 , 4.76196001e+01 , 6.31519102e+01,
                                  7.94681761e+00 , 7.15624016e+01 , 3.74122894e+01 , 7.15624016e+01,
                                  5.00611406e+01 , 4.65670718e+01 , 1.00648284e+00 , 1.31196714e+00,
                                  1.33770129e+00 , 1.35049714e+00 , 1.83495115e-01 , 1.87723502e+00])
        self.data_max_ = np.array([5.19179342e+01 , 7.08148275e+02 , 2.66110555e+01  ,1.01616577e+02,
                                  3.56516190e+01,  1.01616577e+02 , 5.56554258e+01 , 5.01928668e+01,
                                  1.49384167e+00 , 3.25813513e+00,  4.86713804e+00 , 6.09355021e+00,
                                  1.86832391e+00,  5.43312463e+00,  1.40838831e+04,  3.54811305e+07,
                                  5.95660394e+03,  1.81421847e+04 , 5.92214883e+03,  1.81421847e+04,
                                  1.51236134e+04,  1.31817146e+04,  1.15624551e+00 , 1.69567167e+00,
                                  1.96061275e+00,  2.20057181e+00 , 4.64948264e-02 , 2.99667549e+00,
                                  7.52168686e+01 , 2.65608441e+02 , 1.62974980e+01 , 1.06303114e+02,
                                  6.99452618e+01 , 1.06303114e+02 , 7.55991382e+01 , 7.50412426e+01,
                                  1.04105100e+00 , 1.90409810e+00 , 1.97884299e+00 , 2.01343280e+00,
                                  2.38862599e+00 , 8.37616294e+00 , 3.26785255e+01 , 1.89098178e+02,
                                  1.37512973e+01 , 3.71329311e+01 , 1.41975520e+01 , 3.71329311e+01,
                                  3.30995476e+01 , 3.24238442e+01 , 1.16201967e+00 , 1.27451999e+00,
                                  1.48101730e+00 , 1.74555729e+00 ,-6.72460014e-01,  7.38895100e+00,
                                  1.48187802e+03 , 1.57945588e+05 , 3.97423689e+02 , 2.32110000e+03,
                                  1.37995043e+03 , 2.32110000e+03 , 1.52480271e+03 , 1.46142694e+03,
                                  1.37002742e+00 , 3.06695384e+00 , 3.35381536e+00 , 4.20903777e+00,
                                  7.89146203e+00 , 6.32896707e+01 , 7.16958200e+01 , 2.96572825e+02,
                                  1.72212899e+01 , 1.04415843e+02 , 6.54642694e+01 , 1.04415843e+02,
                                  7.22069270e+01 , 7.14616950e+01 , 1.05312887e+00  ,2.02426774e+00,
                                  2.12805550e+00 , 2.17615470e+00 , 2.19272616e+00 , 7.39879712e+00])

        self.min_ = np.min(self.data_min_)
    def fit_transform(self, X):
        """根据拟合的最小值和缩放比例转换数据"""
        if self.min_ is None:
            raise ValueError("This MinMaxScaler instance is not fitted yet. Call 'fit' with some data first.")
        X_std = (X - self.data_min_) / (self.data_max_ - self.data_min_)
        X_scaled = X_std * (self.feature_range[1] - self.feature_range[0]) + self.feature_range[0]
        return X_scaled
def conv3x1(in_planes, out_planes, stride=1):
    """3x3 convolution with padding"""
    return nn.Conv1d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=1, bias=False)
def conv1x1(in_planes, out_planes, stride=1):
    """1x1 convolution"""
    return nn.Conv1d(in_planes, out_planes, kernel_size=1, stride=stride, bias=False)
class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, inplanes, planes, stride=1, downsample=None):
        super(BasicBlock, self).__init__()
        self.conv1 = conv3x1(inplanes, planes, stride)
        self.bn1 = nn.BatchNorm1d(planes)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x1(planes, planes)
        self.bn2 = nn.BatchNorm1d(planes)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity
        out = self.relu(out)

        return out
class ResNet(nn.Module):

    def __init__(self, block, layers, in_channel=1, out_channel=13, zero_init_residual=False):
        super(ResNet, self).__init__()
        self.inplanes = 64
        self.conv1 = nn.Conv1d(in_channel, 64, kernel_size=7, stride=2, padding=3,
                               bias=False)
        self.bn1 = nn.BatchNorm1d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool1d(kernel_size=3, stride=2, padding=1)
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
        self.avgpool = nn.AdaptiveAvgPool1d(1)
        self.dim=512
        layer = []
        layer.append(nn.Dropout(p=0.5))
        self.fc11 = nn.Linear(512, 1024)
        layer.append(self.fc11)
        layer.append(nn.Dropout(p=0.5))
        layer.append(nn.BatchNorm1d(1024))
        layer.append(nn.ReLU(inplace=True))
        self.fc12 = nn.Linear(1024, 1024)
        layer.append(self.fc12)
        layer.append(nn.Dropout(p=0.5))
        layer.append(nn.BatchNorm1d(1024))
        layer.append(nn.ReLU(True))
        self.fc13 = nn.Linear(1024, out_channel)
        layer.append(self.fc13)


        self.classifier = nn.Sequential(*layer)



        for m in self.modules():
            if isinstance(m, nn.Conv1d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
        if zero_init_residual:
            for m in self.modules():
                if isinstance(m, BasicBlock):
                    nn.init.constant_(m.bn2.weight, 0)

    def _make_layer(self, block, planes, blocks, stride=1):
        downsample = None
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = nn.Sequential(
                conv1x1(self.inplanes, planes * block.expansion, stride),
                nn.BatchNorm1d(planes * block.expansion),
            )

        layers = []
        layers.append(block(self.inplanes, planes, stride, downsample))
        self.inplanes = planes * block.expansion
        for _ in range(1, blocks):
            layers.append(block(self.inplanes, planes))

        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)

        x = self.classifier(x)

        return x
    def out_num(self):
        return self.dim
def resnet18(**kwargs):

    model = ResNet(BasicBlock, [2, 2, 2, 2], **kwargs)

    return model


class CnN():
    def __init__(self):
        self.class_name = {0: '进气量不足', 1: '进气量过多', 2: '进气量波动', 3: '高度保护堵塞', 4: '减震器漏气', 5: '绝压堵塞',
               6: '定径孔堵塞', 7: '控制腔泄露到大气', 8: '排气活门堵塞', 9: '余压堵塞',
               10: '座舱泄露', 11: '正常'}
        self.columns = ['大气舱绝压(kPaA)', '高度(m)', '座舱绝压(kPaA)', '座舱余压(kPaA)', '总流量(kg/h)', '控制腔压力(kPaA)']
        "模型保存位置"
        self.maxmin = MinMaxScaler()


    def forward(self,filepath):
        model = resnet18()
        model_stac = torch.load('.\cnnmodel_yuce.pt', map_location='cpu')
        model.load_state_dict(model_stac,strict=False)
        model.eval()

        df = pd.read_excel(filepath)
        feature = get_feature(column=self.columns, data=df)
        feature = self.maxmin.fit_transform(feature)
        torch.set_default_tensor_type(torch.DoubleTensor)
        feature_t = torch.tensor(feature,dtype=torch.float32)
        feature_t = feature_t.unsqueeze(1)
        predicted = model(feature_t)
        output = F.softmax(predicted, dim=1)
        _, pred = torch.max(output, 1)
        pred = pred.numpy()
        predicted = pred[0]
        return self.class_name[predicted]



if __name__ == "__main__":
    k = CnN()
    print(k.forward(r'E:\files\项目\新乡\lpy_guzhangdata_excel\kongzhiqiang_xielou2gaobao\data0_150_0.3mm\28.xlsx'))
