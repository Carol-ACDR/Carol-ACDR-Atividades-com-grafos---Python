from meu_grafo_matriz_adj_dir import *

g_d2_Jd = MeuGrafo(
            ['1', '2', '3', '4', '5', '6', '7', '8'])
g_d2_Jd.adicionaAresta('a0', '1', '4')
g_d2_Jd.adicionaAresta('a1', '1', '5')
g_d2_Jd.adicionaAresta('a2', '2', '4')
g_d2_Jd.adicionaAresta('a3', '3', '5')
g_d2_Jd.adicionaAresta('a4', '4', '6')
g_d2_Jd.adicionaAresta('a5', '4', '8')
g_d2_Jd.adicionaAresta('a6', '4', '7')
g_d2_Jd.adicionaAresta('a6', '5', '7')
g_d2_Jd.adicionaAresta('a6', '3', '8')
print(g_d2_Jd.Khan())

EngC = MeuGrafo(
    ['11', '12', '13', '14', '15', '16', '17','21', '22', '23', '24', '25', '26', '27','31', '32', '33', '34', '35', '36','41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71', '72',
     '72', '73', '74', '75', '81', '82', '83', '84', '85', '91', '92', '93', '94', 'Op1', '101', '102', '103', 'Op2',
     'Op3'])
EngC.adicionaAresta('a0', '11', '21')
EngC.adicionaAresta('a1', '21', '31')
EngC.adicionaAresta('a2', '21', '41')
EngC.adicionaAresta('a3', '31', '51')
EngC.adicionaAresta('a4', '51', '61')
EngC.adicionaAresta('a5', '34', '81')
EngC.adicionaAresta('a6', '35', '81')
EngC.adicionaAresta('a7', '54', '81')
EngC.adicionaAresta('a8', '31', '52')
EngC.adicionaAresta('a9', '43', '62')
EngC.adicionaAresta('a10', '24', '72')
EngC.adicionaAresta('a11', '73', '82')
EngC.adicionaAresta('a12', '83', '92')
EngC.adicionaAresta('a13', '24', '33')
EngC.adicionaAresta('a14', '24', '43')
EngC.adicionaAresta('a15', '24', '53')
EngC.adicionaAresta('a16', '34', '63')
EngC.adicionaAresta('a17', '35', '63')
EngC.adicionaAresta('a18', '63', '73')
EngC.adicionaAresta('a19', '74', '83')
EngC.adicionaAresta('a20', '44', '93')
EngC.adicionaAresta('a21', '45', '93')
EngC.adicionaAresta('a22', '92', '103')
EngC.adicionaAresta('a23', '14', '24')
EngC.adicionaAresta('a24', '15', '24')
EngC.adicionaAresta('a25', '14', '34')
EngC.adicionaAresta('a26', '15', '34')
EngC.adicionaAresta('a27', '24', '44')
EngC.adicionaAresta('a28', '36', '44')
EngC.adicionaAresta('a29', '24', '54')
EngC.adicionaAresta('a30', '31', '64')
EngC.adicionaAresta('a31', '61', '84')
EngC.adicionaAresta('a32', '64', '84')
EngC.adicionaAresta('a33', '61', '94')
EngC.adicionaAresta('a34', '75', '94')
EngC.adicionaAresta('a35', '14', '25')
EngC.adicionaAresta('a36', '15', '25')
EngC.adicionaAresta('a37', '14', '35')
EngC.adicionaAresta('a38', '15', '35')
EngC.adicionaAresta('a39', '36', '45')
EngC.adicionaAresta('a40', '36', '55')
EngC.adicionaAresta('a41', '44', '55')
EngC.adicionaAresta('a42', '55', '65')
EngC.adicionaAresta('a43', '52', '75')
EngC.adicionaAresta('a44', '64', '75')
EngC.adicionaAresta('a45', '75', '85')
EngC.adicionaAresta('a46', '16', '26')
EngC.adicionaAresta('a47', '26', '36')
print(EngC.Khan())

Telematica= MeuGrafo(
    ['11', '12', '13', '14', '15', '16', '17','21', '22', '23', '24', '25', '26', '27','31', '32', '33', '34', '35', '36','37','41', '42', '43', '44', '45', '46', '47', '51', '52', '53', '54', '55', '56', '57', '61', '62', '63', '64', '65', '66','TCC', 'Estagio',
     ])
Telematica.adicionaAresta('a0', '11', '21')
Telematica.adicionaAresta('a1', '12', '22')
Telematica.adicionaAresta('a2', '16', '22')
Telematica.adicionaAresta('a3', '12', '23')
Telematica.adicionaAresta('a4', '16', '23')
Telematica.adicionaAresta('a5', '13', '24')
Telematica.adicionaAresta('a6', '16', '26')
Telematica.adicionaAresta('a7', '21', '31')
Telematica.adicionaAresta('a8', '26', '32')
Telematica.adicionaAresta('a9', '22', '33')
Telematica.adicionaAresta('a10', '23', '33')
Telematica.adicionaAresta('a11', '26', '33')
Telematica.adicionaAresta('a12', '14', '34')
Telematica.adicionaAresta('a13', '25', '35')
Telematica.adicionaAresta('a14', '21', '36')
Telematica.adicionaAresta('a15', '24', '36')
Telematica.adicionaAresta('a16', '31', '41')
Telematica.adicionaAresta('a17', '31', '42')
Telematica.adicionaAresta('a18', '32', '43')
Telematica.adicionaAresta('a19', '32', '44')
Telematica.adicionaAresta('a20', '33', '44')
Telematica.adicionaAresta('a21', '33', '45')
Telematica.adicionaAresta('a22', '21', '46')
Telematica.adicionaAresta('a23', '34', '46')
Telematica.adicionaAresta('a24', '41', '51')
Telematica.adicionaAresta('a25', '41', '52')
Telematica.adicionaAresta('a26', '44', '53')
Telematica.adicionaAresta('a27', '44', '54')
Telematica.adicionaAresta('a28', '37', '55')
Telematica.adicionaAresta('a29', '41', '55')
Telematica.adicionaAresta('a30', '44', '55')
Telematica.adicionaAresta('a31', '42', '61')
Telematica.adicionaAresta('a32', '51', '61')
Telematica.adicionaAresta('a33', '53', '62')
Telematica.adicionaAresta('a34', '55', 'TCC')
Telematica.adicionaAresta('a35', '37', 'Estagio')
Telematica.adicionaAresta('a36', '41', 'Estagio')
Telematica.adicionaAresta('a37', '44', 'Estagio')
print(Telematica.Khan())

Fisica = MeuGrafo(
    ['11', '12', '13', '14', '15', '16', '17','21', '22', '23', '24', '25', '26', '27','31', '32', '33', '34', '35', '36', '37' ,'41', '42', '43', '44', '45','46', '51', '52', '53', '54', '55','56','57', '61', '62', '63', '64', '65','66','68', '71', '72',
     '72', '73', '74', '75','76', '81', '82', '83', '84', '85','86'])
Fisica.adicionaAresta('a0', '11', '21')
Fisica.adicionaAresta('a1', '12', '21')
Fisica.adicionaAresta('a2', '11', '22')
Fisica.adicionaAresta('a3', '12', '22')
Fisica.adicionaAresta('a4', '12', '23')
Fisica.adicionaAresta('a5', '12', '24')
Fisica.adicionaAresta('a6', '14', '24')
Fisica.adicionaAresta('a7', '15', '25')
Fisica.adicionaAresta('a8', '21', '31')
Fisica.adicionaAresta('a9', '23', '31')
Fisica.adicionaAresta('a10', '21', '32')
Fisica.adicionaAresta('a11', '22', '32')
Fisica.adicionaAresta('a12', '23', '33')
Fisica.adicionaAresta('a13', '31', '41')
Fisica.adicionaAresta('a14', '31', '42')
Fisica.adicionaAresta('a15', '32', '42')
Fisica.adicionaAresta('a16', '33', '45')
Fisica.adicionaAresta('a17', '31', '46')
Fisica.adicionaAresta('a18', '41', '51')
Fisica.adicionaAresta('a19', '45', '51')
Fisica.adicionaAresta('a20', '41', '52')
Fisica.adicionaAresta('a21', '42', '52')
Fisica.adicionaAresta('a22', '45', '53')
Fisica.adicionaAresta('a23', '31', '54')
Fisica.adicionaAresta('a24', '43', '55')
Fisica.adicionaAresta('a25', '21', '57')
Fisica.adicionaAresta('a26', '43', '57')
Fisica.adicionaAresta('a27', '51', '61')
Fisica.adicionaAresta('a28', '51', '62')
Fisica.adicionaAresta('a29', '52', '62')
Fisica.adicionaAresta('a30', '21', '63')
Fisica.adicionaAresta('a31', '53', '63')
Fisica.adicionaAresta('a32', '51', '64')
Fisica.adicionaAresta('a33', '56', '66')
Fisica.adicionaAresta('a34', '31', '68')
Fisica.adicionaAresta('a35', '57', '68')
Fisica.adicionaAresta('a36', '61', '71')
Fisica.adicionaAresta('a37', '41', '72')
Fisica.adicionaAresta('a38', '45', '72')
Fisica.adicionaAresta('a39', '66', '73')
Fisica.adicionaAresta('a40', '31', '74')
Fisica.adicionaAresta('a41', '43', '74')
Fisica.adicionaAresta('a42', '41', '76')
Fisica.adicionaAresta('a43', '68', '76')
Fisica.adicionaAresta('a44', '65', '81')
Fisica.adicionaAresta('a45', '74', '82')
Fisica.adicionaAresta('a46', '73', '83')
Fisica.adicionaAresta('a47', '54', '84')
Fisica.adicionaAresta('a48', '71', '84')
Fisica.adicionaAresta('a49', '16', '85')
Fisica.adicionaAresta('a50', '25', '85')
Fisica.adicionaAresta('a51', '51', '86')
Fisica.adicionaAresta('a52', '76', '86')
print(Fisica.Khan())

Const_ed = MeuGrafo(
    ['11', '12', '13', '14', '15', '16', '17','18','21', '22', '23', '24', '25', '26', '27','31', '32', '33', '34', '35', '36', '37','38','41', '42', '43', '44', '45','46','47', '51', '52', '53', '54', '55','56','57', '58', '61', '62', '63', '64', '65','66','67','68', '71', '72',
     '72', '73'])
Const_ed.adicionaAresta('a0', '15', '21')
Const_ed.adicionaAresta('a1', '14', '23')
Const_ed.adicionaAresta('a2', '11', '24')
Const_ed.adicionaAresta('a3', '17', '24')
Const_ed.adicionaAresta('a4', '15', '25')
Const_ed.adicionaAresta('a5', '17', '26')
Const_ed.adicionaAresta('a6', '17', '27')
Const_ed.adicionaAresta('a7', '15', '32')
Const_ed.adicionaAresta('a8', '21', '32')
Const_ed.adicionaAresta('a9', '21', '33')
Const_ed.adicionaAresta('a10', '25', '33')
Const_ed.adicionaAresta('a11', '15', '34')
Const_ed.adicionaAresta('a12', '11', '35')
Const_ed.adicionaAresta('a13', '27', '35')
Const_ed.adicionaAresta('a14', '26', '36')
Const_ed.adicionaAresta('a15', '23', '37')
Const_ed.adicionaAresta('a16', '24', '38')
Const_ed.adicionaAresta('a17', '17', '41')
Const_ed.adicionaAresta('a18', '21', '41')
Const_ed.adicionaAresta('a19', '17', '42')
Const_ed.adicionaAresta('a20', '21', '42')
Const_ed.adicionaAresta('a21', '23', '43')
Const_ed.adicionaAresta('a22', '24', '44')
Const_ed.adicionaAresta('a23', '36', '54')
Const_ed.adicionaAresta('a24', '37', '45')
Const_ed.adicionaAresta('a25', '21', '45')
Const_ed.adicionaAresta('a26', '17', '46')
Const_ed.adicionaAresta('a27', '32', '46')
Const_ed.adicionaAresta('a28', '11', '47')
Const_ed.adicionaAresta('a29', '37', '47')
Const_ed.adicionaAresta('a30', '37', '51')
Const_ed.adicionaAresta('a31', '43', '51')
Const_ed.adicionaAresta('a32', '45', '51')
Const_ed.adicionaAresta('a33', '46', '51')
Const_ed.adicionaAresta('a34', '41', '52')
Const_ed.adicionaAresta('a35', '42', '52')
Const_ed.adicionaAresta('a36', '45', '52')
Const_ed.adicionaAresta('a37', '46', '52')
Const_ed.adicionaAresta('a38', '17', '53')
Const_ed.adicionaAresta('a39', '32', '53')
Const_ed.adicionaAresta('a40', '47', '54')
Const_ed.adicionaAresta('a41', '17', '55')
Const_ed.adicionaAresta('a42', '32', '55')
Const_ed.adicionaAresta('a43', '46', '56')
Const_ed.adicionaAresta('a44', '43', '57')
Const_ed.adicionaAresta('a45', '31', '62')
Const_ed.adicionaAresta('a46', '44', '62')
Const_ed.adicionaAresta('a47', '22', '64')
Const_ed.adicionaAresta('a48', '27', '64')
Const_ed.adicionaAresta('a49', '33', '64')
Const_ed.adicionaAresta('a50', '36', '64')
Const_ed.adicionaAresta('a51', '47', '65')
Const_ed.adicionaAresta('a52', '22', '66')
Const_ed.adicionaAresta('a52', '31', '67')
print(Const_ed.Khan())


Matematica = MeuGrafo(
    ['11', '12', '13', '14', '15', '16', '17','21', '22', '23', '24', '25', '26', '27','31', '32', '33', '34', '35', '36','41', '42', '43', '44', '45','46', '51', '52', '53', '54', '55','56','57', '61', '62', '63', '64', '65','66','67', '71', '72',
     '72', '73', '74', '75','76','77', '81', '82', '83', '84', '85','86','87'])
Matematica.adicionaAresta('a0', '11', '21')
Matematica.adicionaAresta('a1', '11', '22')
Matematica.adicionaAresta('a2', '13', '22')
Matematica.adicionaAresta('a3', '16', '26')
Matematica.adicionaAresta('a4', '21', '31')
Matematica.adicionaAresta('a5', '22', '32')
Matematica.adicionaAresta('a6', '12', '33')
Matematica.adicionaAresta('a7', '12', '34')
Matematica.adicionaAresta('a8', '21', '41')
Matematica.adicionaAresta('a9', '23', '41')
Matematica.adicionaAresta('a10', '23', '42')
Matematica.adicionaAresta('a11', '32', '42')
Matematica.adicionaAresta('a12', '36', '43')
Matematica.adicionaAresta('a13', '34', '44')
Matematica.adicionaAresta('a14', '27', '45')
Matematica.adicionaAresta('a15', '33', '51')
Matematica.adicionaAresta('a16', '12', '52')
Matematica.adicionaAresta('a17', '32', '53')
Matematica.adicionaAresta('a18', '44', '54')
Matematica.adicionaAresta('a19', '44', '55')
Matematica.adicionaAresta('a20', '44', '57')
Matematica.adicionaAresta('a21', '51', '61')
Matematica.adicionaAresta('a22', '52', '62')
Matematica.adicionaAresta('a23', '32', '63')
Matematica.adicionaAresta('a24', '54', '64')
Matematica.adicionaAresta('a25', '46', '65')
Matematica.adicionaAresta('a26', '57', '67')
Matematica.adicionaAresta('a27', '42', '71')
Matematica.adicionaAresta('a28', '22', '72')
Matematica.adicionaAresta('a29', '41', '73')
Matematica.adicionaAresta('a30', '42', '73')
Matematica.adicionaAresta('a31', '64', '74')
Matematica.adicionaAresta('a32', '65', '75')
Matematica.adicionaAresta('a33', '67', '77')
Matematica.adicionaAresta('a34', '62', '81')
Matematica.adicionaAresta('a35', '75', '82')
Matematica.adicionaAresta('a36', '32', '83')
Matematica.adicionaAresta('a37', '74', '84')
Matematica.adicionaAresta('a38', '77', '87')
print(Matematica.Khan())