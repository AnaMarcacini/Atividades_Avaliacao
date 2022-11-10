C:\Users\ahmar\OneDrive\Documentos\Git Hub\Aula 19 - GUI>python -m venv .

C:\Users\ahmar\OneDrive\Documentos\Git Hub\Aula 19 - GUI>cd Scripts

C:\Users\ahmar\OneDrive\Documentos\Git Hub\Aula 19 - GUI\Scripts>activate

(Aula 19 - GUI) C:\Users\ahmar\OneDrive\Documentos\Git Hub\Aula 19 - GUI\Scripts>cd .

(Aula 19 - GUI) C:\Users\ahmar\OneDrive\Documentos\Git Hub\Aula 19 - GUI\Scripts>cd  
C:\Users\ahmar\OneDrive\Documentos\Git Hub\Aula 19 - GUI\Scripts

(Aula 19 - GUI) C:\Usesrs\ahmar\OneDrive\Documentos\Git Hub\Aula 19 - GUI\Scripts>cd ..

(Aula 19 - GUI) C:\Users\ahmar\OneDrive\Documentos\Git Hub\Aula 19 - GUI>python -m pip install streamlit 

(Aula 19 - GUI) C:\Users\ahmar\OneDrive\Documentos\Git Hub\Aula 19 - GUI>python -m streamlit run ./src/main.py 


ctrl + c para a aplicação


git checkout -b aulas15-2

git add.

git commit -m "Aula 15 - introdução"

git push --set-upstream origin aula15

Atividade 3) C:\Users\ahmar\OneDrive\Documentos\Github\Atividades_Avaliacao\Atividade 3>python -m src.tests.teste_user_dao.py

python -m src.tests.teste_user_dao.py

(Atividade 3) C:\Users\ahmar\OneDrive\Documentos\Github\Atividades_Avaliacao\Atividade 3>python -m streamlit run ./src/main.py 
s










(projeto-sqlite) C:\Users\muril\Desktop\projeto-sqlite>python ./tests/teste_controllers.py

C:\Users\ahmar\OneDrive\Documentos\Github\Atividades_Avaliacao\Atividade 3>python ./tests/teste_controllers.py
python: can't open file 'C:\Users\ahmar\OneDrive\Documentos\Github\Atividades_Avaliacao\Atividade 3\tests\teste_controllers.py': [Errno 2] No such file 
or directory



ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 15564 and this is thread id 10996.
Traceback:
File "C:\Users\ahmar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 558, in _run_script
    self._session_state.on_script_will_rerun(rerun_data.widget_states)
File "C:\Users\ahmar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\streamlit\runtime\state\safe_session_state.py", line 73, in on_script_will_rerun
    self._state.on_script_will_rerun(latest_widget_states)
File "C:\Users\ahmar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\streamlit\runtime\state\session_state.py", line 543, in on_script_will_rerun
    self._call_callbacks()
File "C:\Users\ahmar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\streamlit\runtime\state\session_state.py", line 556, in _call_callbacks
    self._new_widget_state.call_callback(wid)
File "C:\Users\ahmar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\streamlit\runtime\state\session_state.py", line 278, in call_callback
    callback(*args, **kwargs)
File "C:\Users\ahmar\OneDrive\Documentos\Github\Atividades_Avaliacao\Atividade 3\src\pages\login.py", line 34, in fui_apertado
    if (verificar.UserController().checkLogin(usuario,senha)):
File "C:\Users\ahmar\OneDrive\Documentos\Github\Atividades_Avaliacao\Atividade 3\./src\controllers\user_controller.py", line 27, in checkLogin
    for user in UsuarioDao.get_instance().get_all():
File "C:\Users\ahmar\OneDrive\Documentos\Github\Atividades_Avaliacao\Atividade 3\./src\dao\usuario_dao.py", line 23, in get_all
    self.cursor = self.conn.cursor()