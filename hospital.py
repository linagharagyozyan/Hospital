class Hospital:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = "{}{}{}{}".format("hospital", "_", self.name.lower(),"@gmail.com")
        self.jobs = []
        self.patients = {}

    def addPatient(self, doctor, patient):
        if patient not in self.patients:
            self.patients[doctor.name + " " + doctor.surname] = patient
        return self.patients

    def getHospitalInfo(self):
        print "Welcome to Hospital", self.name, "\n", "Contact details:","\n", "---------", "\n", "Address:", self.address,"\n", "Email:", self.email, "\n", "Phone:",self.phone

class Job:
    def __init__(self, name):
        self.name = name
        self.doctors = {}

    def addDoctor(self, doctor, job):
        if doctor not in self.doctors:
            self.doctors[doctor.name + " " + doctor.surname] = job.name
        return self.doctors

    def getJobsInfo(self):
        for key in self.doctors:
            print "Doctor:", key, "\n", "Job:", self.doctors[key]

class Doctor:
    def __init__(self, name, surname, speciality, phone):
        self.name = name
        self.surname = surname
        self.email = "{}{}{}{}".format(self.name.lower(), "_", self.surname.lower(), "@gmail.com")
        self.speciality = speciality
        self.phone = phone
        self.patients = []

    def getDoctorInfo(self):
        print "Name: ", self.name, "\n", "Surname: ", self.surname, "\n", "Email: ", self.email,\
            "\n", "Speciality: ", self.speciality, "\n", "Phone: ", self.phone

    def addPatient(self, patient):
            if patient not in self.patients:
                return self.patients.append(patient)
            else:
                print patient.name, patient.surname, "is already in Dr.", self.name, self.surname, "'s list"

    def printPatients(self):
            for k in self.patients:
                print "Patient info", "\n", "---------", "\n", "Name:", k.name, "\n", "Surname:", k.surname, "\n", "Email:", k.email, \
                    "\n", "Disease:", k.disease, "\n", "Status: ", k.status, "\n", "Phone:", k.phone, "\n", "---------"

class Patient:
    def __init__(self, name, surname, disease, status, phone):
        self.name = name
        self.surname = surname
        self.email = "{}{}{}{}".format(self.name.lower(), "_", self.surname.lower(), "@gmail.com")
        self.disease = disease
        self.status = status
        self.phone = phone

def main():

    hospital = Hospital("Nairi", "Paronyan St., 21 Building", "+374-10-537500")
    job1 = Job("Cardiologist")
    doctor1 = Doctor("Armen", "Kirakosyan", "Cardiologist", "+374-77-887788")
    patient1 = Patient("Tigran", "Khachatryan", "High blood pressure", "In progress", "+37477887799")

    hospital.addPatient(doctor1, patient1.name)
    hospital.getHospitalInfo()

    job1.addDoctor(doctor1, job1)
    job1.getJobsInfo()


    doctor1.addPatient(patient1)
    doctor1.getDoctorInfo()
    doctor1.printPatients()
    #doctor1.addPatient(patient1)

main()


#Lina Gharagyozyan, Garik Chilingaryan, Marianna Yesayan, Avet Dabaghyan, Varsik Poghosyan



