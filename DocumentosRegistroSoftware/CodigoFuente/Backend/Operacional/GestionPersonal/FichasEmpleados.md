```
//ENTITY FICHASEMPLEADOS
package com.persona.Backend.Entity.Operational.GestionPersonal;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Operational.GestionHorario.Ficha;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "fichas_empleados")
public class FichasEmpleados extends BaseEntity {

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "empleado_id", nullable = false, unique = false)
	private Empleado empleadoId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "ficha_id", nullable = false, unique = false)
	private Ficha fichaId;

	public Empleado getEmpleadoId() {
		return empleadoId;
	}

	public void setEmpleadoId(Empleado empleadoId) {
		this.empleadoId = empleadoId;
	}

	public Ficha getFichaId() {
		return fichaId;
	}

	public void setFichaId(Ficha fichaId) {
		this.fichaId = fichaId;
	}

}
//IREPOSITORY FICHASEMPLEADOS
package com.persona.Backend.IRepository.Operational.GestionPersonal;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionPersonal.FichasEmpleados;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IFichasEmpleadosRepository extends IBaseRepository<FichasEmpleados, Long>{

}
//ISERVICE FICHASEMPLEADOS
package com.persona.Backend.IService.Operational.GestionPersonal;

import com.persona.Backend.Entity.Operational.GestionPersonal.FichasEmpleados;
import com.persona.Backend.IService.IBaseService;

public interface IFichasEmpleadosService extends IBaseService<FichasEmpleados> {

}
//SERVICE FICHASEMPLEADOS
package com.persona.Backend.Service.Operational.GestionPersonal;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionPersonal.FichasEmpleados;
import com.persona.Backend.IService.Operational.GestionPersonal.IFichasEmpleadosService;
import com.persona.Backend.Service.BaseService;

@Service
public class FichasEmpleadosService extends BaseService<FichasEmpleados> implements IFichasEmpleadosService{

}
//CONTROLLER FICHASEMPLEADOS
package com.persona.Backend.Controller.Operational.GestionPersonal;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionPersonal.FichasEmpleados;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_personal/fichas_empleados")
public class FichasEmpleadosController extends BaseController<FichasEmpleados> {

}


```