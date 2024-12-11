```
//ENTITY MATRICULA
package com.persona.Backend.Entity.Operational.GestionHorario;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Enum.EstadoProceso;
import com.persona.Backend.Entity.Security.Persona;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name="matricula")
public class Matricula extends BaseEntity {
	
	@Column(name = "estado_proceso", length = 40, nullable = false)
	private  EstadoProceso estadoProceso;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "persona_id", nullable = false, unique = false)
	private Persona personaId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "ficha_id", nullable = false, unique = false)
	private Ficha fichaId;

	public EstadoProceso getEstadoProceso() {
		return estadoProceso;
	}

	public void setEstadoProceso(EstadoProceso estadoProceso) {
		this.estadoProceso = estadoProceso;
	}

	public Persona getPersonaId() {
		return personaId;
	}

	public void setPersonaId(Persona personaId) {
		this.personaId = personaId;
	}

	public Ficha getFichaId() {
		return fichaId;
	}

	public void setFichaId(Ficha fichaId) {
		this.fichaId = fichaId;
	}


	
	
}
//IREPOSITORY MATRICULA
package com.persona.Backend.IRepository.Operational.GestionHorario;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionHorario.Matricula;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IMatriculaRepository extends IBaseRepository<Matricula, Long> {

}
//ISERVICE MATRICULA
package com.persona.Backend.IService.Operational.GestionHorario;

import com.persona.Backend.Entity.Operational.GestionHorario.Matricula;
import com.persona.Backend.IService.IBaseService;

public interface IMatriculaService extends IBaseService<Matricula>{

}
//SERVICE MATRICULA
package com.persona.Backend.Service.Operational.GestionHorario;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionHorario.Matricula;
import com.persona.Backend.IService.Operational.GestionHorario.IMatriculaService;
import com.persona.Backend.Service.BaseService;

@Service
public class MatriculaService extends BaseService<Matricula> implements IMatriculaService {

}
//CONTROLLER MATRICULA
package com.persona.Backend.Controller.Operational.GestionHorario;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionHorario.Matricula;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_horario/matricula")
public class MatriculaController extends BaseController<Matricula>{

}

```