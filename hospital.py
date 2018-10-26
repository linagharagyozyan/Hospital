class Node(object):
    def __init__(self):
        self.next = None

class Job(Node):
    def __init__(self, name):
        self.name = name

class Doctor(Node):
    def __init__(self,name,surname,speciality,phone):
        self.name = name
        self.surname= surname
        self.email = "{}{}{}{}".format(self.name.lower(),"_",self.surname.lower(),"@gmail.com")
        self.speciality = speciality
        self.phone = phone

class Patient(Node):
    def __init__(self,name,surname,disease,status,phone):
        self.name = name
        self.surname = surname
        self.email = "{}{}{}{}".format(self.name.lower(),"_",self.surname.lower(),"@gmail.com")
        self.disease = disease
        self.status = status
        self.phone = phone

class Hospital:
    def __init__(self, name, address, phone):
        self.__Jobhead = None
        self.__Doctorhead = None
        self.__Patienthead = None
        self.name = name
        self.address = address
        self.phone = phone
        self.email = "{}{}{}{}".format("hospital","_",self.name.lower(),"@gmail.com")

    def addJob(self, new_job):
        job = Job(new_job)
        if self.__Jobhead == None:
            self.__Jobhead = job
        else:
            temp = self.__Jobhead
            while temp.next is not None:
                temp = temp.next

            newJob = job
            temp.next = newJob

    def addDoctor(self, name, surname, specialty, phone):
        doctor = Doctor(name, surname, specialty, phone)
        if self.__Doctorhead == None:
            self.__Doctorhead = doctor
        else:
            temp = self.__Doctorhead
            while temp.next is not None:
                temp = temp.next

            newDoctor = doctor
            temp.next = newDoctor

    def addPatient(self, name, surname, disease, status, phone):
        patient = Patient(name, surname, disease, status, phone)
        if self.__Patienthead == None:
            self.__Patienthead = patient
        else:
            temp = self.__Patienthead
            while temp.next is not None:
                temp = temp.next

            newPatient = patient
            temp.next = newPatient

    def deleteJob(self, job):
        temp = self.__Jobhead
        while temp.next is not None and temp.next != job:
            temp = temp.next

        temp.next = temp.next.next

    def deleteDoctor(self, doctor):
        temp = self.__Doctorhead
        while temp.next is not None and temp.next != doctor:
            temp = temp.next

        temp.next = temp.next.next

    def deletePatient(self, patient):
        temp = self.__Patienthead
        while temp.next is not None and temp.next != patient:
            temp = temp.next

        temp.next = temp.next.next

    def getHospitalInfo(self):
        print "Welcome to Hospital", self.name, "\n""Contact details:""\n""---------","\n""Address:",self.address,"\n""Email: ",\
              self.email,"\n""Phone: ",self.phone

    def getJobsInfo(self, data):
        temp = self.__Jobhead
        while temp.next is not None and temp != data:
            temp = temp.next
        print "\n",data.name

    def getDoctorInfo(self, data):
        temp = self.__Doctorhead
        while temp.next is not None and temp != data:
            temp = temp.next
        print "\n""Name: ", data.name, "\n""Surname: ", data.surname, "\n""Email: ", data.email, \
              "\n""Speciality: ", data.speciality, "\n""Phone: ", data.phone

    def getPatientInfo(self, data):
        temp = self.__Patienthead
        while temp.next is not None and temp != data:
            temp = temp.next
        print "\n""Patient info", "\n", "---------", "\n", "Name: ", data.name, "\n", "Surname: ", data.surname, "\n", "Email: ", \
              data.email, "\n", "Disease: ", data.disease, "\n", "Status: ", data.status, "\n", "Phone: ", data.phone, "\n", "---------"

def main():
    hospital = Hospital("Nairi", "Paronyan St., 21 Building", "+374-10-537500")

    job1 = Job("Cardiologist")
    hospital.setJobHead(job1)
    job2 = Job("Therapist")
    hospital.appendJob(job2)
    job3 = Job("Surgeon")


    doctor1 = Doctor("Armen","Kirakosyan","Cardiologist","+37477887788")
    hospital.setDoctorHead(doctor1)
    doctor2 = Doctor("Karen","Petrosyan","Cardiologist","+37491070097")
    hospital.appendDoctor(doctor2)
    doctor3 = Doctor("Petros", "Karapetyan","Surgeon","+37498288888")



    patient1 = Patient("Tigran","Khachatryan","High blood pressure","In progress","+37477887799")
    hospital.setPatientHead(patient1)
    patient2 = Patient("Gor","Nersisyan","Diabetes","In progress","+37495000000")
    hospital.appendPatient(patient2)
    patient3 = Patient("Poghos", "Kaputikyan", "Broken toe", "In progress", "+374394822")


    hospital.getHospitalInfo()

    hospital.getDoctorInfo(doctor1)
    hospital.getPatientInfo(patient1)
    hospital.getPatientInfo(patient2)
    hospital.getDoctorInfo(doctor2)



if __name__ == "__main__":
    main()



